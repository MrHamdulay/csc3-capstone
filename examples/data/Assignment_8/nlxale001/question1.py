#Author: NLXALE001
#Date: 6 May 2014
#Assignment8

#create variables and parameters to be used in def pali
global string
string = input("Enter a string:\n")
global pali
pali = True
global indexbegin
indexbegin = 0
global indexend
indexend = len(string)-1

def palin(indexbegin, indexend, pali):
        #test if we have reached the middle and pali us still true
        if pali == True and indexbegin == indexend or indexbegin == (indexend+1):
                print ("Palindrome!")
        #test if pali remains to be true
        elif pali == True and string[indexbegin]==string[indexend]:
                palin(indexbegin+1,indexend-1, pali)
        #end recursion
        else:
                pali == False
                print ("Not a palindrome!") 


palin(indexbegin, indexend, pali)

