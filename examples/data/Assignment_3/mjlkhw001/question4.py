# Program to find all palindromic primes in range
# Khwezi Majola
# MJLKHW001
# 20 March 2014
def palin():
    start = eval(input('Enter the starting point N:\n'))
    end = eval(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    for i in range(start+1, end):
        count = 0
        for z in range(1, i+1):
            if (i % z == 0):
                count += 1
                if count > 2: break
        else:
            r = eval(str(i)[::-1])
            if r == i:
                print(i)    
palin()