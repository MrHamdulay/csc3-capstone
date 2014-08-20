# calculation permutations
#romelon chetty
#mymath.py

def get_integer(s):
    x = input('Enter ' + s + ':\n')
    nut = False
    while nut == False:
        try:
            x = int(x)
            if x < 0:
                x = input('Enter ' + s + ':\n')
                continue
            nut = True
        except:
            nut = False
            x = input('Enter ' + s + ':\n')
    return x

def calc_factorial(x):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        return x * calc_factorial(x - 1)
