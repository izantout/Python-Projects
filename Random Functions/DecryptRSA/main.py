def spaceRemover(text):
    return text.replace(" ","")

def modinv(a,b):
    if (gcd(a,b) != 1):
        raise ValueError("The given values are not relatively prime")
    else:
        for x in range(0,b):
            inverse = ((a % b) * (x % b)) % b
            if inverse == 1:
                return x

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


def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) + 65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2

def decryptRSA(c, p, q, e):
    c = spaceRemover(c)
    n = p * q
    final = ""
    if (gcd((p-1)*(q-1), e) == 1):
        for i in range(0, len(c), 4):
            temp = c[i:i+4]
            temp = (int(temp)**modinv(e,(p-1)*(q-1))) % n
            if (len(str(temp))<4):
                final += digits2letters("0" + str(temp))
            else:
                final += digits2letters(str(temp))
    return final
