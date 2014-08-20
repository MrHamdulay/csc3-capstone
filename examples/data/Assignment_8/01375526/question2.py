message = input('Enter a message:\n')
c=0
def chpair(message):
    global c
    if message == ''  or len(message) == 1:
        return c
    if message[0] == message[1]:
        c+=1
        return chpair(message[2:]) 
    else:
        return chpair(message[1:])
    
        
print('Number of pairs:',chpair(message))