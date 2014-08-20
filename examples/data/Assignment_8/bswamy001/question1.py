"""Amy Bosworth, Assignment 8, Question 1, 6 May 2014"""


#Get a string from the user
w=input("Enter a string:\n")

def palindrome(w):
        
        #if the string is empty or contains one character
        if len(w) == 1 or len(w) == 0:
                return True
        
        elif w[0] == w[-1] and palindrome(w[1:-1]): #recursive step of slicing string
                return True

        else:
                return  False



if palindrome(w)==True:
        print("Palindrome!")
        
else:
        print("Not a palindrome!")