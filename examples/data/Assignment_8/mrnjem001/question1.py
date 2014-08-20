"""Question 1 - check for palindrome
Jembe Moran
11 May 2014"""
def reverse(n): #reverse string
        if n=="":
                return n
        else:
                return(reverse(n[1:])+n[0]) #reverse first letter, reverse rest of string
       
       
x=input("Enter a string:\n")
if x==reverse(x): #check for equality
        print("Palindrome!")
else: print("Not a palindrome!")