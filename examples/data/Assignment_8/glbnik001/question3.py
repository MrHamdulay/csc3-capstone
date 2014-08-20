# 9 May 2014
# Nikhil Gilberts Programme
# Encryption Programme 

lis=[]

def main():
    n = input("Enter a message:\n")
    crypt(n)
    #Check for all !
    #Remove all ! and change them to spaces 
    #Then commence with the following 
    print ("Encrypted message:\n",*lis,sep="")

def crypt(n):
    cryption = ""
    if len(n)<1: # Stops recursion if all characters have been cycled through
        return False
    elif 65<=ord(n[0])<=90:
        lis.append(chr(ord(n[0]))) #adds it to the list if its a capital letter
    else:
        cryption = chr(ord(n[0])+1) #changes all other occurences into the next letter and appends them to the list
        if cryption == "{":
            cryption = "a"
        elif cryption == "!":
            cryption = " "
        elif cryption == "/":
            cryption = "."
        lis.append(cryption)
    crypt(n[1:]) #recursion

main()
