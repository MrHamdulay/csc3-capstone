msg = input("Enter a message:\n")
print("Number of pairs: ", end='')
x=0
def duplicate(msg):
    if (len(msg)==1):
        return True
    elif msg[0] == msg[1]:
        x = x+1
        return duplicate(msg[1:len(msg)])
    else:
        return duplicate(msg[1:len(msg)])
print(x)