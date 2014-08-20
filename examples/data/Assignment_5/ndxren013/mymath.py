

def get_integer(s):
    x = input('Enter '+ s + ':\n')#getting an inout from the user
    keepon = True
    while keepon:
        try:
            x = eval(x)
            if x >= 0:
                break
        except:
            keepon = True
        x = input('Enter '+ s + ':\n')
    return x

def calc_factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i#multiplying to n
    return x
