"""Palindrome Recursion Module"""
#Liam Brodie
#BRDLIA004
#May 2014

print("Enter a string:")

newstring = input("")
    
def palin(newstring):
    """Recursive function to test if a newstring is a palindrome"""
    if newstring == "":                             #Check if string is empty
            print("Not a palindrome!")     
    if len(newstring) == 2 or len(newstring) == 3:  #Check if string is of length 2 or 3
        if newstring[0] == newstring[-1]:
            print("Palindrome!")
        if newstring[0] != newstring[-1]: #Check if the characters at the end and beginning of the string are equal
            print("Not a palindrome!")                          
    if  len(newstring) > 3:                          #Check if string is greater than length 3
        if newstring[0] == newstring[-1]:
            newstring = newstring[1:len(newstring)-1]
            return palin(newstring)
        if newstring[0] != newstring[-1]:          #Check if characters at end & begining of the string are unequal
            print("Not a palindrome!")      
        
palin(newstring)