def prime(n,m):
    prime_numbers = []
    for p in range(2, m+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            prime_numbers.append(p)
    return prime_numbers