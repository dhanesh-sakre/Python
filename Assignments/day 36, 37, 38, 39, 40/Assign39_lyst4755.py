def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)
def sumNOdd(n):
    if n==1:
        return 1
    return 2*n-1+sumNOdd(n-1)
def sumNEven(n):
    if n==1:
        return 2
    return 2*n+sumNEven(n-1)
def sumNSquare(n):
    if n==1:
        return 1
    return n**2+sumNSquare(n-1)
def sumNCube(n):
    if n==1:
        return 1
    return n**3+sumNCube(n-1)