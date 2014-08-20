#assignment 8 Q2 consecutive character counter
#Kavir Ranchod RNCKAV001
#05/05/2014

#Acquire input
message = input("Enter a message:\n")
#initialize counter variable
count = 0
def cons_count(message):
    global count
    #Test if length too short to have pairs
    if len(message) == 1 or len(message) == 0:
        print("Number of pairs:", count)
    #Test whether or not consecutive characters are equal, and add to counter
    elif message[0] == message[1]:
        count += 1
        message=message[2:]
        return cons_count(message)
    else:
        message = message[1:]
        return cons_count(message)
    
cons_count(message)