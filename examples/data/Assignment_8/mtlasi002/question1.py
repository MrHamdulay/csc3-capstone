#Asil Motala
#MTLASI002
#Assignment 8
#Question 1
#27 April 2014

def palindrome(string):
    if string=="" or len(string)==1:                    #breaking condition - no letters left (even length string) or middle letter (odd length string)
        return "Palindrome!"
    elif string[0]==string[-1]:                         #first letter equals last letter
        return palindrome(string[1:len(string)-1])      #check for second letter to second to last letter
    else:
        return "Not a palindrome!"                      #breaking condition for not a palindrome

string=input("Enter a string:\n")                       #get input from user
print(palindrome(string))                               #print result