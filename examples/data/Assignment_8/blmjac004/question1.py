"""checking to see if a string is a palindrome
Jacqueline Blomendahl
8 may 2014"""

string= input("Enter a string:\n") #getting user input

def palindrome(s):  #defining function
    if s == '':
        print("Palindrome!")  #empty string is a palindrome
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0: #checking for same leter at begin and end
            
            return palindrome(s[1:len(s)-1]) #using recursion for the next letter
        else:
            print("Not a palindrome!")


    
palindrome(string)
