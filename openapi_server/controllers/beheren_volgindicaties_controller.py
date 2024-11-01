from datetime import date, datetime, timezone
from http import HTTPStatus

from connexion import NoContent

from .util import _get_default_headers
from ..database.models import VOLGINDICATIES, BURGERSERVICENUMMER, BEGINDATUM, EINDDATUM, _get_volgindicaties_db as get_volgindicaties_db
from ..models import Volgindicatie, VolgindicatieCollectie, VolgindicatieRaadplegen


def get_volgindicatie(token_info, burgerservicenummer):  # noqa: E501
    """Raadpleeg een volgindicatie op een persoon

    Vraag een volgindicatie op van een specifieke persoon.  # noqa: E501

    :param burgerservicenummer: Identificerend gegeven van een ingeschreven natuurlijk persoon, als bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer.
    :type burgerservicenummer: integer

    :rtype: Union[VolgindicatieRaadplegen, Tuple[VolgindicatieRaadplegen, int], Tuple[VolgindicatieRaadplegen, int, Dict[str, str]]
    """
    afnemer_code = token_info['sub']
    headers = _get_default_headers()
    db, volgindicaties_db = get_volgindicaties_db()
    today = date.today()
    data = db.session.execute(db.select(volgindicaties_db)
                              .where(volgindicaties_db.afnemer_code == afnemer_code)
                              .where(volgindicaties_db.burgerservicenummer == burgerservicenummer)
                              .where(volgindicaties_db.begindatum <= today)
                              .where(volgindicaties_db.einddatum > today)).scalars().first()
    if data is None:
        return NoContent, HTTPStatus.NOT_FOUND
    response = VolgindicatieRaadplegen(burgerservicenummer=data.burgerservicenummer, begindatum=data.begindatum, einddatum=data.einddatum)
    return response.to_dict(), HTTPStatus.OK, headers


def get_volgindicaties(token_info):  # noqa: E501
    """Raadpleeg actieve volgindicaties

    Vraag de actieve volgindicaties op van een abonnee. Levert geen volgindicaties met einddatum vandaag of in het verleden.  # noqa: E501


    :rtype: Union[VolgindicatieCollectie, Tuple[VolgindicatieCollectie, int], Tuple[VolgindicatieCollectie, int, Dict[str, str]]
    """
    afnemer_code = token_info['sub']
    headers = _get_default_headers()
    db, volgindicaties_db = get_volgindicaties_db()
    today = date.today()
    data = db.session.execute(db.select(volgindicaties_db).filter_by(afnemer_code=afnemer_code)).scalars().all()
    response = VolgindicatieCollectie([VolgindicatieRaadplegen(burgerservicenummer=row.burgerservicenummer, begindatum=row.begindatum, einddatum=row.einddatum) for row in data])
    return response.to_dict(), HTTPStatus.OK, headers


def upsert_volgindicatie(token_info, burgerservicenummer, volgindicatie=None):  # noqa: E501
    """Plaats, wijzig of beëindig een volgindicatie

    Plaats, wijzig of beëindig een volgindicatie op een specifieke persoon. Als je de persoon nog niet volgt, wordt een volgindicatie geplaatst. Als je de persoon al wel volgt, wordt de volgindicatie gewijzigd. Verwijder de einddatum van een volgindicatie door in de request body een leeg object { } te sturen. Beëindig een volgindicatie door een einddatum gelijk aan de datum van vandaag te sturen.  # noqa: E501

    :param burgerservicenummer: Identificerend gegeven van een ingeschreven natuurlijk persoon, als bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer.
    :type burgerservicenummer: integer
    :param volgindicatie: 
    :type volgindicatie: dict | bytes

    :rtype: Union[VolgindicatieRaadplegen, Tuple[VolgindicatieRaadplegen, int], Tuple[VolgindicatieRaadplegen, int, Dict[str, str]]
    """
    afnemer_code = token_info['sub']
    headers = _get_default_headers()
    db, volgindicaties_db = get_volgindicaties_db()
    today = date.today()
    begindatum = date.today()
    einddatum = date.fromisoformat(volgindicatie.get('einddatum')) or date.today()
    updated_at = datetime.now(timezone.utc)
    data = db.session.execute(db.select(volgindicaties_db)
                              .where(volgindicaties_db.afnemer_code == afnemer_code)
                              .where(volgindicaties_db.burgerservicenummer == burgerservicenummer)
                              .where(volgindicaties_db.begindatum <= today)
                              .where(volgindicaties_db.einddatum > today)).scalars().first()
    if data is None:
        data = volgindicaties_db(afnemer_code=afnemer_code, burgerservicenummer=burgerservicenummer,
                                 begindatum=begindatum, einddatum=einddatum, updated_at=updated_at)
        db.session.add(data)
    else:
        data.einddatum = einddatum
        data.updated_at = updated_at
    db.session.commit()
    response = Volgindicatie(data.einddatum)
    return response.to_dict(), HTTPStatus.OK, headers
