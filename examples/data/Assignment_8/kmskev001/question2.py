"""counting the numbers of pairs in a string
   kevin kumasamba
   05 may 2014"""

message=input("Enter a message:\n")

# problem: count the number of pairs in a string without them overlapping
# smaller problem: find a pair in the string

def pairs(message):
    if message=="":
        return 0
    elif len(message)==1:
        return 0
    elif message[0]==message[1]:
        return 1 + pairs(message[2:])
    else:
        return pairs(message[1:])

print("Number of pairs:", pairs(message))