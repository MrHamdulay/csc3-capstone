"""program that uses a recursive function to count the number of pairs of repeated characters in a string
Thiloshni Moodley
6 May 2014"""

#user asked to enter a message
message = input("Enter a message:\n")

count = 0 # counter to keep track of pairs of characters

def counting_pairs(message):
    global count
    if len(message) <1 or len(message)==1: # executes if length of string is less or equal to 1
        print("Number of pairs:", count)
           
    elif message[0] == message[1]: #when the first two characters are equal
        count = count + 1 #add 1 to the counter
        message = message[2:]
        return counting_pairs(message)
      
    else:
        message = message[1:] #if first two characters not equal, delete first character
        return counting_pairs(message)
    
if __name__=="__main__":
    counting_pairs(message)

