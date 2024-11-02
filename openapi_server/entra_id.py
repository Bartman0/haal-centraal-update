import jwt
from jwt import PyJWKClient


def token_is_valid(tenant_id, audience, token):
    jwks_url = f"https://login.microsoftonline.com/{tenant_id}/discovery/v2.0/keys"
    issuer_url = f"https://login.microsoftonline.com/{tenant_id}/v2.0"
    jwks_client = PyJWKClient(
        jwks_url,
    )
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    return jwt.decode(
        token,
        signing_key.key,
        verify=True,
        algorithms=["RS256"],
        audience=audience,
        issuer=issuer_url,
    )