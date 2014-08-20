message = input("Enter a message:\n")

def countdoubles(message):
    if message == "":
        return 0
    if len(message) < 2:
        return 0
    elif (message[0] == message[1]):
        return 1 + countdoubles(message[2:])
    else:
        return countdoubles(message[1:])

print("Number of pairs:", countdoubles(message))