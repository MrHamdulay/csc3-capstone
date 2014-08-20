#Nicholas Mazower, MZWNIC001
#18/04/2014
#Functions for use in the permutation calculator

#speech is used as the word the input function is 'saying'
def get_integer (x):
    speech= "Enter " + str(x) + ":\n"
    x=input(speech)
    while not x.isdigit ():
        x=input(speech)
    x=eval(x)
    return x


def calc_factorial (y):
    nfactorial=1
    for i in range (1, y+1):
        nfactorial *= i
    return nfactorial