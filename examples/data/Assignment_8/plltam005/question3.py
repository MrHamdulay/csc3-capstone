""" Encrypting message
Tameryn Pillay
9 May 2014 """

# get message input

x = input("Enter a message:\n")
y = len(x)-1

def mes(y):
    
    if y == 0:        # base case
        return chr(ord(x[0])+1)
   
    else:    
            return chr(ord(x[y])+1) + mes(y-1)      # recursive step
    
        
# reversing the encrypted message    
message = mes (y)  
length = len(mes(y))-1    
def palin (length):
       
    if length == 0:
        return message[0]   # base case
    else:
        return message[length] + palin(length-1)   # recursive step
    
k = palin(length) # make function equal to variable 
