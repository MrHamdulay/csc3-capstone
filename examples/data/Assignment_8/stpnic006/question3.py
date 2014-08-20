"""A recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a)
Nicholas Stephenson
11 April 2014"""

alpha="abcdefghijklmnopqrstuvwxyz" #String of the alphabet
encrypted="" #Empty String to be filled with encrypted string
pos=0 #Number to be assigned to letter, so as to encrypt through the function

def encrypt(pos):
    global encrypted #Calls the "encrypted" string that lies utside the function itself
    if s[0] not in alpha[::]: #Function relises on first letter not being capitalised
        encrypted = s #Does not encrypt
    elif pos<len(s) and s[pos] == " " :
        encrypted+= " " #If there is a space, replace it with a space
        return encrypt(pos+1) #Recurse on next position
    elif pos<len(s) and s[pos] == "." :
        encrypted+= "." #If there is a fullstop, replace it with a fulstop
        return encrypt(pos+1) #Recurse on next position    
    
    elif pos<len(s): #if position is within the string
        if s[pos] !="z":
            encrypted+=(alpha[alpha.find(s[pos])+1])
            #replace with following letter, if not z
            return encrypt(pos+1)
            #recurse on to the following position
        elif s[pos] == "z":
            encrypted+=(alpha[alpha.find(s[pos])-25])
            return encrypt(pos+1)
            #replaces z with a
   
            

s=input("Enter a message:\n") #This formatting allows the user to enter the string outside of the recursive function         s for string

encrypt(pos)#calls function after input has entered program
#function runs
print("Encrypted message:\n", encrypted,sep="")
#Prints the encrypted string