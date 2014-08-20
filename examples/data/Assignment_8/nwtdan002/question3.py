'''A Program to shift the order of letters of a string  1 character down
By Daniel Newton
04/05/14'''

def lettershift(string,newstring):  #A function that checks each character of a string, converting it appropriately, then adding it to a new string.
    if string=='':
        return newstring
    if 97<=ord(string[0])<=122:     #Checks if character is in the correct range of lowercase letters.
        if string[0]==" ":  #If there's a " ", no conversion, add to newstring.
            return lettershift(string[1:],(newstring+string[0]))
        elif string[0]=="z":    #The character "z" is added to the newstring as "a"
            return lettershift(string[1:],(newstring+"a"))
        else:   #For every other character, we shift it one down.
            return lettershift(string[1:],newstring+chr(ord(string[0])+1))
    else:   #For characters that aren't in previous range, no changes are made.
        return lettershift(string[1:],newstring+string[0])

newstring=''
string=input("Enter a message:\n")
print("Encrypted message:")     #Asks for use input then runs program to convert.
print(lettershift(string,newstring))
