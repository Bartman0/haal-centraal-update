VOLGINDICATIES: str = "volgindicaties"
BURGERSERVICENUMMER = "burgerservicenummer"
BEGINDATUM = "begindatum"
EINDDATUM = "einddatum"
UPDATED_AT = "updated_at"

models = dict()


def setup(database):

    class VolgindicatiesModel(database.Model):
        _db_instance = database
        __table__ = database.metadata.tables[VOLGINDICATIES]

        @classmethod
        def db_instance(cls):
            return cls._db_instance

    models[VOLGINDICATIES] = VolgindicatiesModel


def _get_volgindicaties_db():
    volgindicaties_db = models[VOLGINDICATIES]
    db = volgindicaties_db.db_instance()
    return db, volgindicaties_db
