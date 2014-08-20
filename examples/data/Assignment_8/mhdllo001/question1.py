word=input("Enter a string:\n")

def check(word):
    if word == '':
        return True
    else:
        if (ord(word[0]) == ord(word[len(word)-1])): #Checks if first and last letters are the same
            
            return check(word[1:len(word)-1])#Recursion to take out the first and last letters if they the same
        else:
            return False
if(check(word)==True):
    print("Palindrome!")
else:
    print("Not a palindrome!")