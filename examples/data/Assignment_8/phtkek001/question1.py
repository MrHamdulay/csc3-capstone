"""Kekolo Phetla 
phtkek001"""

def palin(string,index):
    if len(string)/2 >=index:
        if string[index]==string[-1-index] and palin(string,index+1) == "Palindrome!":
            return "Palindrome!"
        else:
            return "Not a palindrome!"
        
    else:
        return "Palindrome!"


string=input("Enter a string:\n")
print(palin(string,0))
