"""
Prashanth Sridharan
SRDPRA001
Assignment 08
Question 01
"""
def Reverse(i): #Fuction defined for reversing the palindrome with the parameter i
    if i == "": #step to terminate the recursion 
        return i
    else: #the recursive steps.
        return (Reverse(i[1:])+i[0])
    
ini = input("Enter a string:\n")
if ini == Reverse(ini):
    print("Palindrome!")
else:
    print("Not a palindrome!")
