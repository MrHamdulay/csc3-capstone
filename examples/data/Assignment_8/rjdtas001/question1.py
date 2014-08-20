#Tashiq Rajdev(RJDTAS001
#Assignment 8
#Recursion
#Question 1

def palindrome(string):
    if len(string)== 0:
        print("Palindrome!")
        return
    elif string[0]==string[-1]:
        palindrome(string[1:-1])
        
    else:
        print("Not a palindrome!")
        return
        
string = input("Enter a string:\n" )
if string != "":
    palindrome(string)

        
        
        
        
