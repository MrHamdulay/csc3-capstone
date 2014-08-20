""""palindrome checker
clare walker
5 may 2014"""



def palin(string):
    if len(string)==1: #if at end, just return first letter
        return string
    else:
        return string[-1] + palin(string[:-1]) #reverse word

string=input("Enter a string:\n")
if string == palin(string):
    print("Palindrome!")
else:
    print("Not a palindrome!")