def bezout_coeffs(a, b):
    r = 1
    s = 1
    s1 = 0
    s2 = 1
    t = 0
    t1 = 1
    t2 = 0
    flag = False
    
    firsta = a
    firstb = b
    gcd = 0
    
    if abs(b) > abs(a):
        temp = abs(a)
        a = abs(b)
        b = temp
        firsta = b
        firstb = a
        flag = True
    
    if a != 0 and b != 0:
        while(r > 0):
            if a > b:
                q = a // b
                r = a - q * b
                print(a, "=", q, "*", b, "+", r)
                s2 = s - q * s1
                t2 = t - q * t1
            if r > 0:
                a = b
                b = r
                s = s1
                s1 = s2
                t = t1
                t1 = t2

            if (b>0):
                gcd = b

    else:
        if a == 0:
            gcd = b
        else:
            gcd = a
    if flag:
        temp2 = s1
        s1 = t1
        t1 = temp2
    return {firsta: s1, firstb: t1}
