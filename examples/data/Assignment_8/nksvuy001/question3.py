"""program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a)
vuyolwethu nksoi
4 may 2014"""

msg=input("Enter a message:\n") #get input from user
def encode(msg):
    if len(msg)<1: #if the string entered is empty ie. Base Case
        return " " #return the empty string
    if msg[0].islower()==False: #want to evaluate all the letters and nothing else, therefore by changing to lower case, this will work with only the letters, as only letters can be changed to upper or lower case
        return msg[0] + encode(msg[1:]) #if the first letter is not in lower case, move onto the next position of the string ie. recursive step
    elif msg[0]=="z": #defining an obvious, since z is the last letter, the next letter has to be a
        return "a" + encode(msg[1:]) #recursive step: go and check next letter and see if same conditions are met      
    else:
        msg_1=(ord(msg[0])+1) #changing the letter to its UNICODE value then adding one to it
        msg_1=chr(msg_1) #changing the now encoded letter to a letter again
        return msg_1 + encode(msg[1:]) #recursive step: return the first encoded letter and start the program again, starting from the next position in the string

print("Encrypted message:")
print(encode(msg)) #print
    
    