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
      
