"""Program to create an encrypted message
Runako Muzwidzwa
06/05/2014"""
x=input("Enter a message:\n")
def encryption(x):
    if x=="":
        return ""
    else:
        first=x[0]
        if first.isalpha() and first.islower():#to check whether th letter is in alphabet and in lower case
            if first=="z":#if yu add 1 to chr it will start giving characters
                return "a"+ encryption(x[1:])
            else:
                first=chr(ord(first)+1)#to change the letter to the one afer it in alphabet
        return first + encryption(x[1:])
print("Encrypted message:")
print(encryption(x))