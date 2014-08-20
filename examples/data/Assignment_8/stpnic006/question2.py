"""Recursive function to count the number of pairs of repeated characters in a string
Nicholas Stephenson
11 April 2014"""

def repeat(s): #s for String
    if s== "" or len(s) == 1: #If string has no-, oronly a single character/s then there cannot be repeatition
        return 0
    elif len(s) == 2: #A string of length 2 can only have 1 pair, whereby the first- and second characters are equal
        if(ord(s[0])) == (ord(s[1])): #Checks to see if they are equal
            return 1 #If equal
        else: 
            return 0 #If not equal
    
    
    elif len(s)>2: #If String length is greater than 2
        if (ord(s[0])) == (ord(s[1])): #If 1st character is equal to the seconf character
            return 1+ repeat(s[1::1]) #Add one and recurse
        
        
        elif(ord(s[0])) != (ord(s[1])): #If 1st character does NOT equal second character
            return 0+ repeat(s[1::1]) #Does NOT add one, but does recurse 
        
#Results, above, a return for use elsewhere in the program

        
s = input("Enter a message:\n") #This formatting allows the user to enter the string outside of the recursive function
repeat(s)

print("Number of pairs:", repeat(s)) #prints out the result result
