"""Program to count pairs
Claudia Pastellides 
8 May 2014"""

def pairfinder(string, tracker):
    length = len(string)
    if length > 1:
        if string[0] == string[1]:
            tracker += 1 #adds to current pair count
            pairfinder(string[2:],tracker)
        else:
            pairfinder(string[1:],tracker)
    else:
        print("Number of pairs:", str(tracker))

message = input("Enter a message:\n") #gets user input
pairfinder(message,0) #sets tracker to 0 and sets message as string