'''recursive to calculate number of letter pairs in string
nic findlay
04 may 2014'''

def pairs(words):
    if len(words) == 0:
        return 0
    if len(words) == 1:
        return 0
    elif words[0] == words[1]:
        return 1 + pairs(words[2:])
    else:
        return pairs(words[1:])
        
    

if __name__ =="__main__": 
    
    words = input('Enter a message:\n')
    print('Number of pairs:', pairs(words))