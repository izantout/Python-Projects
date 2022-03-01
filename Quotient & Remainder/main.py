def div_alg(a, d):
    q = a // d                                                        # Quotient is integer division
    r = a % d
    if r + (d * q)==a:                                                # Remainder is modulo
        return {'quotient' : q, 'remainder' : r}
