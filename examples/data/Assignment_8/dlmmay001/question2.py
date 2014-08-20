
def pairs(x):
    
    if len(x) <= 1:
        return 0
        
    elif x[0] == x[1]:
        return 1 + pairs(x[2:])
    
    else:
        return 0 + pairs(x[1:])
x = input('Enter a message:\n')    
print('Number of pairs:', pairs(x))                 