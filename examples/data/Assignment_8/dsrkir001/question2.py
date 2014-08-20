#Program that uses a recursive function to count the number of pairs of repeated characters in a string. 
#Kiran Desraj - DSRKIR001
#5 May 2014

#User is prompted to enter a message

message = input('Enter a message:\n')

number = 1

def pairs(string):
    global number
    if string == '':
        return number
    else:

#Checks if the length of string is greater than 1 and the first letter in the word is the same as the next ketter
        
        if len(string) > 1 and string[0] == string[1]:
            number += 1          
            
#Recursive function            
            
            return pairs(string[2:len(string)])
        
        else:
            return pairs(string[1:len(string)])



#prints the number of pairs

print ('Number of pairs:', (pairs(message)-1))