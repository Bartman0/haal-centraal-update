import os
from enum import StrEnum
from typing import NamedTuple

from sqlalchemy import URL


class Environment(StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class AppConfig(NamedTuple):
    ENVIRONMENT: str
    SQLALCHEMY_DATABASE_URI: str
    SECRET_KEY: str
    DEBUG: bool = False


def get_config(environment) -> AppConfig:
    if environment not in Environment:
        raise EnvironmentError(
            f"Unknown environment type {environment} in APP_ENVIRONMENT env var"
        )
    environment = environment.upper()
    uri = URL.create(
        drivername=os.environ[f"SQLALCHEMY_DRIVER_{environment}"],
        host=os.environ[f"POSTGRESQL_HOST_{environment}"],
        username=os.environ[f"POSTGRESQL_USERNAME_{environment}"],
        password=os.environ[f"POSTGRESQL_PASSWORD_{environment}"],
        database=os.environ[f"POSTGRESQL_DATABASE_{environment}"],
        port=os.environ[f"POSTGRESQL_PORT_{environment}"],
    )
    return AppConfig(
        ENVIRONMENT=environment,
        SECRET_KEY=os.environ[f"SECRET_KEY_{environment}"],
        DEBUG=not(environment == Environment.PRODUCTION),
        SQLALCHEMY_DATABASE_URI=uri,
    )


ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "development")
CONFIG = get_config(ENVIRONMENT)
