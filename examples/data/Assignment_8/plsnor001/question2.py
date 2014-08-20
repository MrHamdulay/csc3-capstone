'''Uses a recursive function to count the number of pairs of repeated characters in a string
Noko 
06 May 2014'''

def message(word):
    if len(word) < 2:
        return 0
    
    else:
        if word[0]==word[1]:
            return 1 + message(word[2:])
        
        else:
            return message(word[1:])

mes=input('Enter a message:\n')        

print('Number of pairs:',message(mes))