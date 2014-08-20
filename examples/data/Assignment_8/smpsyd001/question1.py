#Palindrome with recursion
#6 May 2014
#Sydney Simpson



    
def function(string,number):
    if len(string)==0:
        return string
    if number==len(string)-1:
        return string[number]
    else:
        new= function(string,number+1)+string[number]
        return new
        

string=input("Enter a string: \n")

    
if (function(string,0))==string:
    print ("Palindrome!")
else:
    print("Not a palindrome!")
