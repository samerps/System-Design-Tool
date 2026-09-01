from pathlib import Path
import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

PASSWORD = b"test-password"
ITERATIONS = 600_000


def derive_key(password: bytes, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256",
        password,
        salt,
        ITERATIONS,
        dklen=32,
    )


def encrypt_file(input_file: str, output_file: str):
    input_path = Path(input_file)
    output_path = Path(output_file)

    data = input_path.read_bytes()

    # Random 128-bit salt
    salt = os.urandom(16)

    # Derive AES-256 key
    key = derive_key(PASSWORD, salt)

    # Random 96-bit AES-GCM nonce
    nonce = os.urandom(12)

    encrypted = AESGCM(key).encrypt(
        nonce,
        data,
        None,
    )

    # File format:
    #
    # [16 byte salt]
    # [12 byte nonce]
    # [ciphertext + 16 byte GCM authentication tag]
    #
    output_path.write_bytes(
        salt + nonce + encrypted
    )

    print(
        f"{input_path} -> {output_path} "
        f"({len(data)} -> {len(salt + nonce + encrypted)} bytes)"
    )


encrypt_file("app.py", "app.py.enc")
encrypt_file("inverter_base.py", "inverter_base.py.enc")
encrypt_file("assets/logo.png", "assets/logo.png.enc")