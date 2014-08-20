# Julian van Rensburg
# Assignment 8 Question 1
# palindrome program

def palindrome(word,p):
    str(word)
    if len(word)>4:
        if not p == (len(word) - 1 - p):
            if word[p] == word[len(word)-1-p]:
                p += 1
                palindrome(word,p)
                return True
            else:
                return False
    elif len(word)==4:
        if word[0:2] == word[2:4]:
            return True
        else:
            return False
    elif len(word)==3:
        if word[0] == word[2]:
            return True
        else:
            return False
    

        
        
def main():
    a = input("Enter a string:\n")
    b = 0
    c = palindrome(a,b)
    
    if c:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
    
main()
    