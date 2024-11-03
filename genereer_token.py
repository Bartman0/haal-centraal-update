#!/usr/bin/env python3

import argparse
from openapi_server import auth

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subject", required=True, help="subject van het token, oftewel de code van de afnemer")
args = parser.parse_args()

print(auth.encode_token(args.subject, [auth.VOLGINDICATIES_ROLE]))
