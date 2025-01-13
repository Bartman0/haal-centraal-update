import os
from datetime import date
from http import HTTPStatus

from connexion import NoContent
from psycopg_pool import ConnectionPool
from sqlalchemy import URL

from openapi_server import util
from .util import _get_default_headers
from ..config import ENVIRONMENT
from ..database.models import _get_volgindicaties_db as get_volgindicaties_db
from ..models import (
    GewijzigdePersonenHalCollectie,
    GewijzigdePersonenHalCollectionLinks,
    HalLink,
    Foutbericht,
    BadRequestFoutbericht,
    InvalidParams,
)

BRP_PERSONEN_URL = (
    "https://benk-brp-{omgeving}.amsterdam.nl/api/v1/brp/personen/{burgerservicenummer}"
)
BRP_WIJZIGINGEN_URL = "https://benk-brp-{omgeving}.amsterdam.nl/api/v1/brpupdate/wijzigingen?vanaf={datum}"


psycopg_connection_info = URL.create(
    drivername="postgresql",
    host=os.environ[f"POSTGRESQL_HOST_{ENVIRONMENT.upper()}"],
    username=os.environ[f"POSTGRESQL_USERNAME_{ENVIRONMENT.upper()}"],
    password=os.environ[f"POSTGRESQL_PASSWORD_{ENVIRONMENT.upper()}"],
    database=os.environ[f"POSTGRESQL_DATABASE_{ENVIRONMENT.upper()}"],
    port=os.environ[f"POSTGRESQL_PORT_{ENVIRONMENT.upper()}"],
)
connection_pool = ConnectionPool(
    psycopg_connection_info.render_as_string(hide_password=False), max_size=10
)
connection_pool.wait()


def get_gewijzigde_personen(token_info, vanaf=None):  # noqa: E501
    """Raadpleeg personen met gewijzigde gegevens

    Vraag een lijst op met burgerservicenummers van personen met gewijzigde gegevens.  # noqa: E501

    :param vanaf: Alleen personen waarbij gegevens zijn gewijzigd op of na deze datum worden geleverd.
    :type vanaf: str

    :rtype: Union[GewijzigdePersonenHalCollectie, Tuple[GewijzigdePersonenHalCollectie, int], Tuple[GewijzigdePersonenHalCollectie, int, Dict[str, str]]
    """
    vanaf = util.deserialize_date(vanaf)
    if vanaf is None:
        return (
            BadRequestFoutbericht(
                code="paramsRequired",
                detail="The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modification.",
                status=HTTPStatus.BAD_REQUEST.value,
                title="Vanaf datum moet worden opgegeven met een geldige datum.",
                type="https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1",
                invalid_params=InvalidParams(
                    type="https://vng.nl/realisatie/api/validaties/datum",
                    name="vanaf",
                    code="date",
                    reason="Waarde is geen geldige datum",
                ),
            ).to_dict(),
            HTTPStatus.BAD_REQUEST,
        )
    afnemer_code = token_info["sub"]
    headers = _get_default_headers()
    db, volgindicaties_db = get_volgindicaties_db()
    today = date.today()
    bsn_selectie = (
        db.session.execute(
            db.select(volgindicaties_db.burgerservicenummer)
            .where(volgindicaties_db.afnemer_code == afnemer_code)
            .where(volgindicaties_db.begindatum <= today)
            .where(volgindicaties_db.einddatum > today)
        )
        .scalars()
        .all()
    )
    if bsn_selectie is None:
        return NoContent, HTTPStatus.NOT_FOUND
    response = []
    # TODO move data driver to Databricks instead of PostgreSQL
    with connection_pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TEMP table bsn_selectie(burgerservicenummer bigint, CONSTRAINT bsn_selectie_pkey PRIMARY KEY (burgerservicenummer)) ON COMMIT DROP"
            )
            with cursor.copy(
                "COPY bsn_selectie(burgerservicenummer) FROM STDIN"
            ) as copy:
                for bsn in bsn_selectie:
                    copy.write_row((bsn,))
            cursor.execute(
                """
                SELECT l.burgerservicenummer FROM bsn_lijst l 
                JOIN bsn_selectie s ON s.burgerservicenummer = l.burgerservicenummer
                WHERE l.updated_at >= %s
                """,
                (vanaf,),
            )
            for record in cursor:
                response.append(record[0])
        collectie = GewijzigdePersonenHalCollectie(
            links=GewijzigdePersonenHalCollectionLinks(
                _self=HalLink(
                    href=BRP_WIJZIGINGEN_URL, templated=True, title="BRP API Personen"
                ),
                ingeschreven_persoon=HalLink(
                    href=BRP_PERSONEN_URL, templated=True, title="BRP API Personen"
                ),
            ),
            burgerservicenummers=response,
        )
    return collectie.to_dict(), HTTPStatus.OK, headers
