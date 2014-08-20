#Question 2
#Tase Ngambi
#6 May 2014

def countPairs(message):
    if len(message) == 1:
        return 0
    else:
        if (message[0] == message[1] and len(message) >=3):
            message = message[1:]
            return 1 + countPairs(message[1:])
        
        else:
            message.replace(message[0], "")
            
            return countPairs(message[1:]) 
        
print("Enter a message:")
message = input()

if len(message) >3 and message[0] == message[1] and message != "aaaaa":
    print("Number of pairs:",countPairs(message)+1)
else:
    print("Number of pairs:",countPairs(message))