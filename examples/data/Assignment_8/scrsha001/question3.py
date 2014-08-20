#Shaaheen Sacoor SCRSHA001
#Program to encode a message by shifting one letter over
# 8 may 2014

def Encode(s):
    if s == '':
        return ""
    else:
        if s[0] == "z":
            return "a" + Encode(s[1:])
        elif s[0].islower() is True:
            return chr(ord(s[0])+1) + Encode(s[1:])
        else:
            return s[0] + Encode(s[1:])
        
def main():
    s = input("Enter a message:\n")
    x = Encode(s)
    print("Encrypted message:")
    print(x)
    
main()