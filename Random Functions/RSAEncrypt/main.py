def mod_exp(b, n, m):
    if ((b > 0) and (n > 0) and (m > 0)):
        x = 1
        p = b % m
        for i in range(0,n):
            if (n & 1):
                x = (x * p) % m
            n = n >> 1    
            p = (p * p) % m
        return x
    else:
        return 0

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

def encryptRSA(text,a,b):
    text = text.replace(" ", "") # remove space from text
    firsta = a # save inputed a
    firstb = b # save inputed b
    final = ""
    temp = b #from here 
    b = 26
    m = b
    q = 0
    r = 1
    gcd = 0
    
    if (type(a) == int and type(b) == int and a>b):
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
                gcd = a # to here is to find the gcd of a and 26


        if (gcd == 1):
            Error = False
            while(len(text)%2 != 0): # If the text is shorter than 4*r, we add X to the end
                text = text + "x"
                print(text)
            fullNum = ""
            for i in range(0,len(text),1): # Make every letter in the text upper case
                text = text.upper()
                fullNum += letters2digits(text[i]) 
            for i in range(0, len(fullNum), 4):
                m = fullNum[i:i+4]
                if(len(str(mod_exp(int(m),firstb,firsta)))<4):
                    t = '0' + str(mod_exp(int(m),firstb,firsta))
                else:
                    t = str(mod_exp(int(m),firstb,firsta))
                final = final + t + " "
            final = final[:-1]
        else:
            Error = True
        if Error:
            raise ValueError
        else:
            return final
    else:
        raise ValueError
