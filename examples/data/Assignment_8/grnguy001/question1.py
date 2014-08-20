#Checking if input is a palindrome
#Done by Guy Green 
#Assignment 8 
#Question 1

def palindrome(t):
    #convert t to string
    t=str(t)
    #Base Case
    if t == '':
        return True
    else:
        if t[0] == t[-1]: #Checking first index is equal to last index
            return palindrome(t[1:-1]) #Recursion
        else:
            return False #Breaking Out if it isn't a palindrome



if __name__=="__main__": #So I can import it in question 4
    entry=input("Enter a string:\n")
    if palindrome(entry):
        print("Palindrome!")
    else:
        print("Not a palindrome!")

