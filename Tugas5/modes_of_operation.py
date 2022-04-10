import requests as r

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

req = r.get(f"{BASE_URL}/encrypt_flag")
val = req.json()
ciphertext = val["ciphertext"]

req = r.get(f"{BASE_URL}/decrypt/{ciphertext}")
val = req.json()
hex = val["plaintext"]

print(bytearray.fromhex(hex).decode())