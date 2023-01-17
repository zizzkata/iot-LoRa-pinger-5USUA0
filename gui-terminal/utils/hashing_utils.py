import hashlib

def hash_string(string: str) -> str:
    hasher = hashlib.sha256()
    hasher.update(string.encode())
    return hasher.hexdigest()