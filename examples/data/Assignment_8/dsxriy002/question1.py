#Question 1 - Assignment 8
#Riya Desai
#7 May 2014


#ask user to enter a string
string=input("Enter a string:\n")

#define the function
def Palindrome(string):
    
    if string =="":
        return ""
    
    elif string==" ":
        return " "
    
    else:
        
        return string[-1] + Palindrome(string[0:len(string)-1])

#check to see whether the word spelt backwards is equal to the word spelt forward
output=Palindrome(string)

if output==string:
    print("Palindrome!")
else:
    print("Not a palindrome!")