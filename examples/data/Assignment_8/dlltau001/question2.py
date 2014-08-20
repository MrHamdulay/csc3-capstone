"""Question 2
Assignment 8
CSC1015F

Return amount of letter pairs with no overlap in a string using recursion
"""

message = input("Enter a message:\n")
def pairs(message,count):
    if message == "":
        print("Number of pairs: ",count,sep="")
    else:
        if message[0:1] == message[1:2]:
            return pairs(message[2:],count + 1)
        else:
            return pairs(message[1:],count)
        
pairs(message,0)