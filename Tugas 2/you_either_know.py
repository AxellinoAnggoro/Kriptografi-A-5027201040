from pwn import xor

data = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
unhex = bytes.fromhex(data)

print(xor (unhex, 'crypto{}'.encode()))
print(xor (unhex, 'myXORkey'.encode()))