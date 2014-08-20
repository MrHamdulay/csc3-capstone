# a program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
# mashau zwivhuya
# 5 may 2014
# get input from user
name=input("Enter a message:\n")
# printing title message
print("Encrypted message:")
def encrypt(name):
    if len(name)==0:
        return 0
    n=name[0]
    if n=="z":
        n="a"
    elif n.islower():
        n=ord(n)+1
        n=chr(n)
    if n=="!":
        n=" "
    # printing encrypted message
    print(n,end="")
    encrypt(name[1:])
encrypt(name)