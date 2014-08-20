'''Program to encrypt messages using recursion
Tinotenda Chemvura CHMTIN004
03 May 2014'''

#__________________________Program Starts Here__________________________________

def encrypt_msg(msg):
    #return and empty string if the string length is zero
    if len(msg) == 0:
        return ""
    elif len(msg) > 0:
        #if the 1st character is 'z', replace it with 'a', then slice off the 1st character and use as the next input in the function
        if msg[0] == "z":
            return 'a' + encrypt_msg(msg[1:])
        #if the character is a space or fullstop, return a space or fullstop
        elif msg[0] == " ":
            return " " + encrypt_msg(msg[1:])
        elif msg[0] == ".":
            return "." + encrypt_msg(msg[1:])        
        #in the case when 1st character is 'Z'
        #elif msg[0] == "Z":
         #   return 'A' + encrypt_msg(msg[1:])        
        elif msg[0] in "qwertyuiopasdfghjklzxcvbnm":
            return chr(ord(msg[0])+1) + encrypt_msg(msg[1:])
        elif msg[0] in "QWERTYUIOPASDFGHJKLZXCVBNM":
            return msg[0] + encrypt_msg(msg[1:])
#print the output of the program
msg = input("Enter a message:\n")
print("Encrypted message:\n"+encrypt_msg(msg))
#___________________________Program Ends Here___________________________________