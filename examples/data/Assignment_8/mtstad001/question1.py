""" Tadiwanashe Mautsa
program to check for palindrome using recursion
6th of May"""
#want a function that checks a string for similarities
S=input("Enter a string:\n")
S=S.lower()
def pal(S):
    if S=="":
        return S
    else:
        return pal(S[1:]) + S [0] #reverses the function
#print(pal(S)==S)
if pal(S)==S:
    print("Palindrome!")
else:
    print("Not a palindrome!")
pal(S)    
    
#now want to create a function that reverses to see 
#if the reversed thing is equal to the original string