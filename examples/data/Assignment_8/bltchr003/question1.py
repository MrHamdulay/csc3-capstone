"""CHRIS BOLTON
11/05/2014"""

def reverser(string): 
    if string=="":
        return string 
    else:
        return (reverser(string[1:])+string[0]) 
    
word = input("Enter a string:\n")

if word==reverser(word): 
    
    print("Palindrome!")
    
else:
    print("Not a palindrome!")