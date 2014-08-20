#Recursion to count the number of repeated pairs in a character
#Devaksha Pillay
#4 May 2014

message = input("Enter a message:\n")
count = 0

def repeated_characters(message):
    
    if message == "" or len(message)<=1:
        # if input is blank or there is only one letter left
        return 0
    else:
        if message[0] == message[1]:
            return repeated_characters(message[2:]) + 1
        else:
            return repeated_characters(message[1:])
       
pairs = repeated_characters(message)
print("Number of pairs:", pairs)