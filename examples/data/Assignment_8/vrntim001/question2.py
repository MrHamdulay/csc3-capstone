'''recursion no. pairs
Tim Mostert
06.05.14'''

# checks if first 2 characters are pairs, if so count + 1 and and recalls minus those characters
# else recalls minus first character
def pairs(message,count):
    
    
    if len(message) == 1:
        print("Number of pairs:", count)
    elif len(message) == 2 and message[0] == message[1]:
        count += 1
        print("Number of pairs:", count)
    elif message[0] == message[1]:
        count += 1
        pairs(message[2:],count)     
    else:
        pairs(message[1:],count)
    
        
        
message = input("Enter a message:\n")
count = 0
pairs(message,count)        