"""encrypting messages
ringo shima
8/5/14"""


def encrypt(mssg,mssg2):
    
    if mssg == "": #base case
        return mssg2 #return nothing
    
    elif mssg[0] == " ":
        mssg2 += " " #add " " to string
        return encrypt(mssg[1:],mssg2) #go to next value
    elif mssg[0] =="z":
        mssg2 += "a" #want to make loop of alphabet
        return encrypt(mssg[1:], mssg2)
    
    elif mssg[0] == ".":
        mssg2 += mssg[0] #dont want `/` instead of `.`
        return encrypt(mssg[1:], mssg2)
    else:
            
        mssg2 += chr(ord(mssg[0])+1) #change ord to +1
        return encrypt(mssg[1:], mssg2)
   
def main():
    x = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
    mssg = input("Enter a message:\n")
    if mssg [0] in x: #if upper(thought about using mssg.isupper()-didnt know how)
            print("Encrypted message:\n" + mssg)    
    else:
        print("Encrypted message:\n" + encrypt(mssg,""))
    #if str(mssg).isupper:
     #   print("Encrypted message:\n" + mssg)
   # elif str(mssg).islower:
   
              
main()

    