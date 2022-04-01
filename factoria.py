def fac_iterative(n):
    fac = 1
    for i in range(n):
        fac = (i+1)*fac
        return fac
fac_iterative(n)