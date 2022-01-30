def mod_exp(b, n, m):
    if b > 0:
        pass
    else:
        b = 0
    if n > 0:
        pass                    # Checks if theres any negative number and changes it to 0
    else:
        n = 0
    if m > 0:
        pass
    else:
        m = 0

    if b * n * m > 0:
        print(b ** n % m)
    else:                                      # If one of the numbers is 0 the answer is 0
        print("0")

