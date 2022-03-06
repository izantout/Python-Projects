def spaceRemover(text):
    return text.replace(" ","")
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
        letters += chr(int(digit) + 65)    # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters
    

def affineEncrypt(text, a, b):
    print(gcd(a,26))
    print(spaceRemover(text))
    text = spaceRemover(text)
    if(gcd(a,26)==1):
        encryptedtext = ""
        for i in range(0,len(text),1):
            if(len(str((a*int(letters2digits(text[i]))+b)%26))<2):
                encrypted = "0" + str((a*int(letters2digits(text[i]))+b)%26)
            else:
                encrypted =str((a*int(letters2digits(text[i]))+b)%26)
            encryptedtext += digits2letters(encrypted)
            encrypted = ""
        return encryptedtext
    else:
        raise ValueError("The given key is invalid. The gcd(a,26) must be 1.")
