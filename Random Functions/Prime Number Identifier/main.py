def primes(a,b):
    set = {4,3}
    if a<1:
        Error = True
    elif b<a:
        Error = True
    elif (a<=b and a>=1):
        set.clear()
        Error = False
        for j in range(a,b+1):
            isPrime = True
            for i in range(2,j):
                if (j%i)==0:
                    isPrime = False
            if isPrime == True:
                set.add(j)
    if (Error==True):
        raise ValueError
    else:
        return set
