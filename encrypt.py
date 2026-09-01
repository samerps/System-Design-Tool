from pathlib import Path
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY = b"01234567890123456789012345678901"

input_file = Path("inverter_base.py")
output_file = Path("inverter_base.py.enc")

data = input_file.read_bytes()

nonce = os.urandom(12)

encrypted = AESGCM(KEY).encrypt(
    nonce,
    data,
    None
)

output_file.write_bytes(nonce + encrypted)

print(f"Encrypted {input_file} -> {output_file}")
print(f"Original size: {len(data)} bytes")
print(f"Encrypted size: {len(nonce + encrypted)} bytes")