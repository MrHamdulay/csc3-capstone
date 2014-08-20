message=input("Enter a message:\n")
def pairs(message):
    if len(message)<=1:
        return 0
    elif message[0]==message[1]:
        return 1+pairs(message[2:])
    else:
        return pairs(message[1:])
print("Number of pairs:",pairs(message))
