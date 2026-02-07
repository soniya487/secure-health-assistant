import os, hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def get_aes_key():
    k = os.environ.get("AES_KEY")
    if not k:
        raise RuntimeError("AES_KEY not set")
    k_bytes = k.encode()
    if len(k_bytes) < 32:
        # pad
        k_bytes = k_bytes.ljust(32, b'0')
    return k_bytes[:32]

def encrypt_bytes(data: bytes) -> bytes:
    key = get_aes_key()
    iv = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ct, tag = cipher.encrypt_and_digest(data)
    return iv + tag + ct

def decrypt_bytes(pack: bytes) -> bytes:
    key = get_aes_key()
    iv = pack[:12]
    tag = pack[12:28]
    ct = pack[28:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    return cipher.decrypt_and_verify(ct, tag)

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()
