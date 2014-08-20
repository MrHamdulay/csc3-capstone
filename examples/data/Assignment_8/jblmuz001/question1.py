# Muzammil Jable
# Assignment 8
# 4 May 2014

def Checkpal(s):           #checks if sentence is a palindrome
    if len(s)==1:
            return True    
    if len(s)==2:
        if s[0]==s[1]:
            return True
    
    recString=s[1:-1]
    if s[0]!=s[-1]:
        return False                #returns false if not palindromic
    elif s[0]==s[-1]:
        return Checkpal(recString)

def main():
    s=input("Enter a string:\n")     
    bool_value=Checkpal(s)
    if bool_value:
        print("Palindrome!")
    elif not bool_value:
        print("Not a palindrome!")
        
if __name__=="__main__":

    main()