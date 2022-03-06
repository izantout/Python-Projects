def spaceRemover(text):
    return text.replace(" ","")

def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

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

def modinv(a,b):
    if (gcd(a,b) != 1):
        raise ValueError("The given values are not relatively prime")
    else:
        for x in range(0,b):
            inverse = ((a % b) * (x % b)) % b
            if inverse == 1:
                return x
            
def affineDecrypt(ciphertext, a, b):
    ciphertext = spaceRemover(ciphertext)
    decryptedText = ""
    for i in range(0,len(ciphertext),1):
        decrypted = (modinv(a,26) * (int(letters2digits(ciphertext[i])) - b)) % 26
        if (len(str(decrypted)) < 2):
            decryptedText += digits2letters("0" + str(decrypted))
        else:
            decryptedText += digits2letters(str(decrypted))
    return decryptedText
