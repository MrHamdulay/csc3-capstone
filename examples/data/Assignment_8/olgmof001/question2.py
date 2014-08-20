"""Tofunmi Olagoke
5 May 2014
Programme on finding repitions"""

position=0

def pairs(message):
    global position
    if len(message)<=1:
        print(position)
    elif message[0]==message[1]:
        position = position+1
        return pairs(message[2:])
    else:
        return pairs(message[2:])

message = input("Enter a message:\n")
print("Number of pairs: ",end ="")
pairs(message)