"""YONELA FORD
FRDYON001
04 MAY 2014"""
#get an input from user

def palin(string,x):
    #if there is a space or just one character, then it is a palindrome
    if len(string)/2 >=x:
        if string[x]==string[-1-x] and palin(string,x+1) == "Palindrome!":
             return "Palindrome!"  
        else:
             #when the check fails, the string is not a plaindrome
             return "Not a palindrome!"        
    #else keep checking the last and first characters of the string (looping recursively)

    else:
        return "Palindrome!"
if __name__ == "__main__":    
    string=input("Enter a string:\n")
    print(palin(string,0))