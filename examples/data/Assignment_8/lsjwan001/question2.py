# program uses recursive function to count the number of pairs of repeated characters
# Wandile Lesejanes
# 8 May 2014

def pairs(message):
    #get the pairs of letters in a string and count them
    c=0
    if len(message)==0 or len(message)==1:
        return 0
    else:
        if message[0]==message[1]:
            return (c+1) +pairs(message[2:])
        else:
            return c +pairs(message[1:])
  
#print out the number of pairs in a given string      
message=input("Enter a message:\n")
print("Number of pairs:",pairs(message))
    