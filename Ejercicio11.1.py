def mcd(a, b):
    if b != 0:
        return mcd(b, a % b)
        
    