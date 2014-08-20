"""Program to encrypt a message
tinashe choga
5/4/2014"""
#function to encrypt the text
def encrypt(string):
    convert=ord(string[0])+1
    new=chr(convert)# converting the first letter of each recursive step to the next
    
    if len(string)==1:
        if string[0]==string[0].upper():
            return string[0].upper()
        elif string[0]=="z":
            return "a"
        else:
            return new
    elif string[0]==string[0].upper():#if uppercase return the letter as it is
        return string[0]+ encrypt(string[1:])
    elif string[0]=="z":
        return "a" + encrypt(string[1:])# if z converting to a
    else:
        return new + encrypt(string[1:])

#printing out the result from the process
string=input("Enter a message:\n")
y=encrypt(string)
print("Encrypted message:")
print(y)