import hashlib

hasher = hashlib.sha256()

def hash_string(string: str) -> str:
    hasher.update(string.encode())
    return hasher.hexdigest()