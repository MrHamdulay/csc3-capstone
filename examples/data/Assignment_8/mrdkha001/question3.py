"""Program that encryptes a message
Khanyisile Morudu
06 May 2014"""

#input
message = input("Enter a message:\n")

#variable
global s_new
s_new = ""
#recursive function
def encrypt_s(s):
    if len(s) < 1:
        return ""
    elif s[0] == "z":
        return s_new + "a" + encrypt_s(s[1:len(s)])
    elif (s[0].lower() == s[0]) and (s[0].isalpha() == True): 
        return  s_new + (chr(ord(s[0]) + 1)) + encrypt_s(s[1:len(s)])
    else:
        return s_new + s[0] + encrypt_s(s[1:len(s)])
                                    
                                     
#output
print("Encrypted message:")
print(encrypt_s(message))
