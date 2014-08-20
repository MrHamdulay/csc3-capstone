"""Tumi Mkhawana
9 May 2014
Assignment 8 question 1"""

#define a function with parameters string and index
def palin(string,index):
    
    if len(string)/2 >=index:
        if string[index]==string[-1-index] and palin(string,index+1) == "Palindrome!":
            return "Palindrome!"  
        else:
            return "Not a palindrome!"        
    else:
        return "Palindrome!"

if __name__ == "__main__":    
    string=input("Enter a string:\n")
    print(palin(string,0))