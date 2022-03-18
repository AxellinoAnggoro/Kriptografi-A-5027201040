import pwn

string = "label"

flag = pwn.xor (string, 13)

print (flag)