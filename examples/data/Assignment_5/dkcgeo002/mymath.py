__author__ = 'George de Kock'
#2014-04-13


def get_integer(n):
    k=n
    while not n.isdigit():
        print("Enter ",k,":",sep="")
        n = input("")
    return eval (n)


def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial