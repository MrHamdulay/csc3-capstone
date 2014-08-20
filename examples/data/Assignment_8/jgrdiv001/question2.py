"""program to count the number of repeated characters in a string
author : DIVAN JAGERS
date: 9 May 2014"""
string = input("Enter a message:\n") #prompts the user to input string that will be used
def Pcount(string):
    if len(string) == 0:      #base case
        return 0
    else:
       #to get the first characters

        if string[0:1] == string[1:2]: #to check if the first characters are equal 
            return 1 + Pcount(string[2:])# counts the pairs with the recursive step
        else:
            return Pcount(string[1:])
print("Number of pairs:",Pcount(string))