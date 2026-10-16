def moms(p, tax):
    if tax <= 0 or tax > 100:
        raise ValueError("Illegal tax")

    if p > 1_000_000:
        raise ValueError("Absurdly high price")

    if p < 0:
        p = -p

    return p * (1 + tax / 100)
