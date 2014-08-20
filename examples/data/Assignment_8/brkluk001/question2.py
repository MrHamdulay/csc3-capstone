'''Program to check if how many pairs there are in a string using recursion
8 May 2014
Luke Barker'''


def pair_search(x):
    if len(x) < 2:    #if the sting is 1 character, then there ia no pairs 
        return 0
    elif x[0] == x[1]:    #checks whether the character next to the first character, recursively
        return 1+pair_search(x[2:])    #if they are it goes to looks for the next pair
    else: 
        return 0+pair_search(x[1:])   #if there is no pair it only goes to the next letter to look for a pair
x = input('Enter a message: \n')
print('Number of pairs:', pair_search(x))

#if x[0].isupper:
    #return 0+pair_search(x[1:])