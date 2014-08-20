"""Count number of pairs of repeated characters
Kumaran Reddy
8 May 2014"""

message=input("Enter a message:\n")
def repeats(message):
    if len(message) < 2: #Base test-if less than two characters,then can't repeat
        return 0
    elif message[0]==message[1]: #if first character is same as second character
        return repeats(message[2:]) + 1 #return 1 and then cut string shorter from third character
    else:
        return repeats(message[1:]) + 0 #returns 0 if not true and cuts string from second character
    
print("Number of pairs:" ,repeats(message)) #returns how many pairs