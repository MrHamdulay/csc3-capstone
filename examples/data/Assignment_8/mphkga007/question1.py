""" palidrome using recursion
kenneth mphele
04/04/2014"""

sreverse=''
string=input("Enter a string:\n")
scopy=string
def palindrome(scopy):
    global sreverse 
    #check if there is a string and if the reverse string is equal to the original one
    if len(scopy)==0 and sreverse==string:
        return "Palindrome!"
    else:
        #checks the string is not an empty string
        if len(scopy)!=0:
            sreverse+=scopy[-1] #makes the reverse copy of the string
           
            return palindrome(scopy[:-1])
        elif len(scopy)==0 and string!=sreverse: #checks if after there is no string is the reverse the same as the original
            return "Not a palindrome!"
    

print(palindrome(string))