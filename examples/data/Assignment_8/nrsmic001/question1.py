"""Program to detemine if word is palindrome
Micaela Narasmulu
09 May 2014"""

string=input("Enter a string:\n")

def check(string):
    if string == '': #if input is empty string then still palindrome
        return True
    
    else:
        if (ord(string[0]) == ord(string[len(string)-1])): #check if word is palindrome
            
            return check(string[1:len(string)-1])
        
        else:
            return False
        
if(check(string)==True):
    print("Palindrome!")
    
else:
    print("Not a palindrome!")