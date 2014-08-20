"""encrypting phrases
   Rivoningo Seweya
   08 May 2014"""
msg=input("Enter a message:\n")
def twos(msg):
    if msg.islower():
        if len(msg)==0:
            return msg
        else:
            if msg[0] in "., !?":
                print(msg[0],end="")
                twos(msg[1:])
            elif msg[0] =="z":
                encrypt= ord(msg[0])-25
                print(chr(encrypt),end="")
                twos(msg[1:])
            else:
                encrypt= ord(msg[0])+1
                print(chr(encrypt),end="")
                twos(msg[1:])  
    else:
        print(msg) 
print("Encrypted message:\n",end="")
twos(msg)            