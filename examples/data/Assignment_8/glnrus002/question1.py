#GLNRUS002
#Assignment 8
#Question 1
#Right program that tests palindromes

def palendrome(s):#actua; test done
    if len(s) < 2: 
        return True
    if s[0] != s[-1]: 
        return False
    return palendrome(s[1:-1])
        
#Get input    
sentence=input("Enter a string:\n")
output=palendrome(sentence)
if output==True:
    print("Palindrome!")
else:
    print("Not a palindrome!")