#Program to check character repetition in a string
#Tyrone Arnold
#9 April 2014

def repeat(s):
    if s == "": #empty string has no repeated chraracters
        return 0
    
    if len(s) == 1: #string of length one has no repeated characters
        return  0
    
    elif len(s) == 2:   #string length of 2 can only have on repeated character
        if (ord(s[0])) == (ord(s[1])): #checks if first and second character are equal
            return 1
        else:
            return 0    
    
    elif len(s)>2: #string length of greater than 2
        if (ord(s[0])) == (ord(s[1])): #if first chr equals second chr        
            return 1+ repeat(s[1::1]) #add one and recurse
        
        elif (ord(s[0])) != (ord(s[1])): #if first chr does not equal second chr
            return 0+ repeat(s[1::1]) #do not add one but recurse
        

s = input("Enter a message:\n") #input string
repeat(s)

print("Number of pairs:", repeat(s)) #print result