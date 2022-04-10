from Crypto.Cipher import AES
import binascii
import hashlib
import requests
import sys

req = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
hex = req.json()["ciphertext"]

word = requests.get('https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words')
word = word.text
word = word.split("\n")

for i in word:
    att_key = hashlib.md5(i.encode()).hexdigest()
    ciphertext = bytes.fromhex(hex)
    key = bytes.fromhex(att_key)
    cipher = AES.new(key, AES.MODE_ECB)

    try:
        decrypted = cipher.decrypt(ciphertext)
        dec = binascii.unhexlify(decrypted.hex())
        if dec.startswith('crypto{'.encode()):
            print(dec.decode('utf-8'))
            sys.exit(0)

    except ValueError as o:
        continue