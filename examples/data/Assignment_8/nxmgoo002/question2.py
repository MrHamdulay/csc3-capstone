'''this programm checks if there are any pairs
Nxumalo Goodman
09 May 2014'''


def double (w):
    #base case
    if w == '':
        return 0 #if the string is empty it returns zero
    elif len(w) < 2:
        return 0 # if the string is less then zero returns zero
    #recursion step
    elif w[0] == w[1]:
        return 1 + double(w[2:])
    else:
        return double(w[1:])
    
#prompt the user to enter the string    
w = input('Enter a message:\n')
double(w)
print('Number of pairs:',double(w))