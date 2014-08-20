#question3
# Author: justin Valsecchi
#2014/05/08
def encrypt(s):
    if len(s) == 1:
        if s.islower(): #testing if the string is lowercase
            if s == 'z': 
                return 'a' #returning a value for 'z' to 'a'
            else:
                return chr(ord(s) + 1) #giving the ord value of one char, to the next ord of the next char
        else:
            return s
    else:
        return encrypt(s[0]) + encrypt(s[1:])

string = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(string))