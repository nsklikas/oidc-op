from typing import List

DIVIDER = ";;"


def session_key(*args, sid_enc_jwks=None) -> str:
    if sid_enc_jwks:
        # do encryption and return
        pass
    # else:
    return DIVIDER.join(args)


def unpack_session_key(key: str, sid_enc_jwks=None) -> List[str]:
    if sid_enc_jwks:
        # do decryption and return
        pass
    # else:
    return key.split(DIVIDER)


class Revoked(Exception):
    pass


class MintingNotAllowed(Exception):
    pass
