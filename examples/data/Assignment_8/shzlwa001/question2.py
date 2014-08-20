def pairs_count (message,pairs) :
    if len(str(message)) <= 2:
        if len(str(message)) == 2:
            if message[0] == message [1] :
                pairs = 1
            else: pairs = 0
            
        else : pairs = 0
        return pairs
        
    else :
        
        
        #pairs =  pairs_count(message) + pairs_count(message[0:2]) 
        return (pairs + pairs_count(message[2:],pairs))
    
    
    
            
message = input('Enter a message:\n')
pairs = 0

print('Number of pairs:',pairs_count (message,pairs))

