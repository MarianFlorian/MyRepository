
def returnChange(rest, denominations):
    toGiveBack = [0] * len(denominations)
    mi = denominations[::-1]
    for indice in range(mi):
        valoare = mi[indice]
        while valoare <= rest:
            rest = rest - valoare
            toGiveBack[indice] += 1
    return toGiveBack[::-1]


#def fib(n):

    f = [0] * n
    f[0] = 1
    f[1] = 1
    if n <= 2:
        return 1
    for i in range(2,n):
        f[n] = f[n-1] + f[n-2]
#    return f



if __name__ == "__main__":
    fib(4)