'''A program that gets a string from the user and use the recursion function to find if the string is palindromic or not
Jacob Ntesang
06 May 2014'''

S = input("Enter a string:\n")
#Get the string from trhe user
def Palindrome(S):
    if S == "":
        return "Palindrome!"
    elif S[0] == S[-1]:
        return Palindrome(S[1:-1])
    else:
        return "Not a palindrome!"
    
print(Palindrome(S))