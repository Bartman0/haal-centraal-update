import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="BRP Update API",
    author_email="",
    url="",
    keywords=["OpenAPI", "BRP Update API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Met deze API kun je opvragen welke door jou gevolgde personen zijn gewijzigd in de BRP. Je kunt je abonneren op een persoon die je wilt volgen, en je kunt opvragen welke personen door jou worden gevolgd. Je kunt deze API gebruiken in combinatie met de BRP bevragen API, bijvoorbeeld om lokale kopiegegevens actueel te houden.  Om lokale kopiegegevens actueel te houden kun je de volgende procedure volgen: 1. Zet de volgindicatie. 2. Vraag de persoonsgegevens op met de BRP Bevragen API. 3. Vraag periodiek (bijvoorbeeld dagelijks) de wijzigingen op met GET /wijzigingen. Gebruik parameter \&quot;vanaf\&quot; met de datum dat de laatste/vorige keer wijzigingen waren gevraagd. Voor elk burgerservicenummer in de response \&quot;burgerservicenummers\&quot; vraag je de persoonsgegevens op met de BRP Bevragen API. 
    """
)

