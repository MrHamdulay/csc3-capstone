# question1.py
# a program with a recursive function to calculate whether 
# or not a string is a palindrome
# Thomas Konigkramer
# 5 May 2014

def palindrome(s):
    
    # if confirmed that string is palindrome (thus empty) print "Palindrome!"
    if s == "":
        return True 
    
    #"""Check for if length of s equals 1"""
        
    # checking if first letter is equal to last
    # repeating process if true
    elif s[0:1] == s[-1:]:
        return palindrome(s[1:-1])
    
    else:
        return False

if __name__ == "__main__":   
    s = input("Enter a string:\n")
    if palindrome(s):
        print("Palindrome!")  
    else:
        print("Not a palindrome!")