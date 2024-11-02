"""
More on JWT tokens: https://jwt.io/
"""

import logging
from datetime import datetime, timedelta, timezone
from random import randrange

import jwt
from werkzeug.exceptions import Unauthorized

from openapi_server.config import CONFIG

ALGORITHM = "HS256"
VOLGINDICATIES_ROLE = "benk-brp-volgindicaties"


def decode_token(token):
    try:
        token_info = jwt.decode(
            token,
            CONFIG.SECRET_KEY,
            options={"require": ["iss", "iat", "exp", "sub", "roles"]},
            algorithms=[ALGORITHM],
        )
        if VOLGINDICATIES_ROLE not in token_info["roles"]:
            logging.error(f"Not authorized to use this API")
            return None
        return token_info
    except jwt.DecodeError:
        logging.debug(f"Token decoding error")
        return None
    except jwt.ExpiredSignatureError:
        logging.debug(f"Token signature expired")
        return None
    except jwt.InvalidIssuerError:
        logging.debug(f"Invalid token issuer")
        return None
    except jwt.InvalidTokenError:
        logging.debug(f"Unknown error")
        return None


def encode_token(subject, roles=list()):
    timestamp_now = int(datetime.now(timezone.utc).timestamp())
    token = jwt.encode(
        {
            "iss": "haal-centraal-update",
            "iat": timestamp_now,
            "exp": timestamp_now + timedelta(hours=24).total_seconds(),
            "sub": subject,
            "roles": roles,
            # "aud": "haal-centraal-update",
            # "jti": timestamp_now + randrange(1_000_000, 10_000_000-1)
        },
        CONFIG.SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return token
