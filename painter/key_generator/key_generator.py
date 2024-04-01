import base64

def make_key_for_fernet(key: str) -> bytes:
    while len(key) < 32:
        key += key
    key = key[:32]
    key = base64.urlsafe_b64encode(bytes(key, "ascii"))
    return key
