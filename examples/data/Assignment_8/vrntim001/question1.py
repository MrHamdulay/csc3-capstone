'''Recursion palindrome
Tim Mostert
06.5.14'''

# checks if first letter = last letter, if True recalls function without those letters
# defines palindrome if message length = 0,1

def recursivep(string):
    if len(string) < 2:
        print("Palindrome!")
    elif string[0] == string[-1]:
        recursivep(string[1:len(string)-1])
    elif string[0] != string[-1]:
        print("Not a palindrome!")
    
    
string = input("Enter a string:\n")
recursivep(string)
    
