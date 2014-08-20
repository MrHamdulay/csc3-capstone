# Question 2
# 5 May 2014
# Richard van Gysen
# number of pairs

# Enter a message
message = input("Enter a message:\n")
# define function pairs
def pairs(message):
    # if nothing return 0
    if len(message) == 1:
        return 0
    # recursive step. if true for first carry on and add 1
    elif len(message) == 2:
        if message[0] == message[1]:
            return 1
        else:
            return 0
    elif message[0] == message[1]:
        return 1 + pairs(message[2:])
    # if not first two, carry on and dont add 1
    else:
        return pairs(message[1:])
print("Number of pairs:",pairs(message))
