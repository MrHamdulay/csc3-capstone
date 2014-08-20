#Dean Bunce
#Program to find palindromes using recursion
#3 May 2014


#Get input from user
string=input("Enter a string: \n")


#Reverse the string using recursion    
def reverse(string):

    string_2=string
    
    if string=="":
        
        return string_2
        
    else:
        
        string_2=string[-1]
        
        return string_2 + reverse(string[:-1])

#Check if the reverse string is the same as the string
if string==reverse(string):
    
    print("Palindrome!")
    
else: print("Not a palindrome!")