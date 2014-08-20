#Palindrome
#Sofia Palmer
#4 May 2014

string = input("Enter a string: \n")

#reverse string
def reverse(string):
    if string == "":
        return string
    else:
        return reverse(string[1:]) + string[0]
#if reverse of string == string --> palindrome  
def palindrome(string):
    if (string == reverse(string)):
        print("Palindrome!")
    else:
        print("Not a palindrome!")

palindrome(string)
    

    
        
        
    
