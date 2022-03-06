def gcd(a, b):
    q = 0
    r = 1
    gcd = 0
    
    if abs(b) > abs(a):
        temp = abs(a)
        a = abs(b)
        b = temp
    
    if a != 0 and b != 0:
        while(r > 0):
            if a > b:
                q = a // b
                r = a - q * b
            if r > 0:
                a = b
                b = r

            if (b>0):
                gcd = b

    else:
        if a == 0:
            gcd = b
        else:
            gcd = a
    return gcd

def modinv(a,m):
    print("The GCD is: ", gcd(a,m))
    if (gcd(a,m) != 1):
        raise ValueError("The given values are not relatively prime")
    else:
        for x in range(0,m):
            inverse = ((a % m) * (x % m)) % m
            if inverse == 1:
                return x
