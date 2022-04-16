import requests
import json
from Crypto.Util.strxor import strxor

cookie_url = 'https://aes.cryptohack.org/flipping_cookie/get_cookie/'
val_cookie = requests.get(cookie_url).json()["cookie"]
decode = bytes.fromhex(val_cookie[:32])

def val_flag(val_cookie,decode):
	url='https://aes.cryptohack.org/flipping_cookie/check_admin/'
	response=requests.get(url+'/'+val_cookie+'/'+decode)

	return response.json()

text=b'admin=False;expi'
forge_text=b'admin=True;expir'

xor_result=strxor(decode,text)
forge_iv=strxor(xor_result,forge_text).hex()

print(val_flag(val_cookie[32:],forge_iv)["flag"])
