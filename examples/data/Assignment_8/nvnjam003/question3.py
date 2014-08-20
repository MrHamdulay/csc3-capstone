def conversion(n): #Conversion
    if len(n) == 1 and n[0] in "abcdefghijklmnopqrstuvwxy": #If one letter and lower != z
        return chr(ord(n[0]) + 1) #Normal conversion
    if len(n) == 1 and n[0] == 'z': #If z, return a
        return 'a'
    elif n[0] in "abcdefghijklmnopqrstuvwxy": #If first letter and lower != z
        return chr(ord(n[0])+1) + conversion(n[1:]) #Return converted letter and rest of string converted
    elif n[0] == 'z': #Same as above, first letter z
        return 'a' + conversion(n[1:])
    elif len(n) > 1: #If not letter, do nothing
        return n[0] + conversion(n[1:])
    else:
        return n[0]
    
userString = input ("Enter a message:\n") #Printing result
print ("Encrypted message:\n" + conversion(userString))