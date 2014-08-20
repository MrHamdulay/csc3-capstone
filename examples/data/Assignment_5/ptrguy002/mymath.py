from functools import reduce

def get_integer(n):
    while True:
        try:
            a = int(input("Enter " + n + ":\n"))
            if a < 0:
                continue
            return a
        except ValueError:
            continue

def calc_factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))
