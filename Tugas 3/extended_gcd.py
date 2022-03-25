def extended_gcd(p, q):
    if p == 0:
        return q, 0, 1
    else:
        gcd, x, y = extended_gcd(q % p, p)
        return gcd, y - (q // p) * x, x
 
if __name__ == '__main__':
    gcd, x, y = extended_gcd(26513, 32321)
    print(min(x,y))