# Shane Horsley
# Program to check if a string is a palindrome
# 5 May 2014
def palindrome(x): #funtion to check if input is a palindrome
    if len(x) == 1 or len(x) ==0: #if a string is 1 or 2 characters its a prime
        return True
    elif x[0]==x[len(x)-1]: #check first and last letter of string
        return palindrome(x[1:len(x)-1])
    else:
        return False #if the first and last arent equal can be palindrome

if __name__== "__main__": #so i can use the function in question 4
    string = input("Enter a string:\n")
    if palindrome(string) == True: 
        print("Palindrome!")
    else: 
        print("Not a palindrome!")
