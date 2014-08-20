#Thea Sitek, STKTHE002
#09.05.2014

def pairs(sentence):
    
    length = len(sentence)
    if length <=1:
        return 0
    else:
        if sentence[0] == sentence[1]:
            return 1 + pairs(sentence[2:])
        else:
            return pairs(sentence[1:])


message = input('Enter a message: \n')
print('Number of pairs:', pairs(message))
