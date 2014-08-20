# program that uses a recursive function to count the number of pairs of repeated characters in a string.
# Retselisitsoe Monyake
# 7 May 2014

# a function to count the number of pairs
def count_pairs (message):
    if len(message)==1:
        return 0
    elif len(message)==2:
        if message[0]==message[1]:
            return 1
        else:
            return 0
    elif message[0] == message[1]:
        return 1 + count_pairs(message[2:])
    else:
        return 0 + count_pairs(message[1:])
"""printing out the number"""
message=input("Enter a message:\n")
y=count_pairs(message)  #calling the function and assigning it to a variable
print("Number of pairs:",y)

 
        
 
        
   

