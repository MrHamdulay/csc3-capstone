userInput = input("Enter a message:\n")

sec = userInput[1:]
numPairs = 0

def pairs(fir,sec,numPairs):
    
    if(len(sec)>1):
        if(fir[:1] == sec[:1]):
            numPairs+=1
            return pairs(sec[1:], sec[2:],numPairs)
        else:
            return pairs(sec, sec[1:],numPairs)
    elif(len(sec) == 1):
        if(fir[:1] == sec[:1]):
                numPairs+=1
                return pairs(sec, sec[1:],numPairs)  
        else:
                return pairs(sec, sec[1:],numPairs)        
    else:
        return numPairs

pair = pairs(userInput,sec,numPairs)
print("Number of pairs:",pair)