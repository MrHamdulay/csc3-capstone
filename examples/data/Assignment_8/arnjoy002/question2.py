#Joy Arendse-Gorvalla
def Pairs (s): #creating a function that will determine number of pairs in a sentence
    if len(s) == 1 or len(s) == 0:
        return 0
    if s[0] == s[1]:
        return 1 + Pairs(s [2:])
    else:
        return 0 + Pairs(s[1:])

message = input ("Enter a message:\n") #ask user to enter a message    
print ("Number of pairs:",Pairs(message)) #displays number of pairs in that message
