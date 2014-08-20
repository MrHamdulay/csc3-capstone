# BLKAT005
# Kate Bell
# 6 May 2014 

def convert(s):
    #base case
    if len(s)==1:
        if s.islower():
            if s=='z':
                return 'a'
            else: return chr(ord(s)+1)
        else: return s
    else:
        if s[0].islower():
            if s[0]=='z': 
                return 'a' + convert(s[1::])
            else: 
                return chr(ord(s[0])+1) + convert(s[1::])
        else: return s[0] + convert(s[1::])
    

message = input("Enter a message:\n")
print("Encrypted message:")
print(convert(message))