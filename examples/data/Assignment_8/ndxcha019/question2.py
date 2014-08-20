'''Program to find pairs in a string
Luke Naude
7 may 2014'''

pairs=0
message=input('Enter a message:\n') #get message
letter1=0
letter2=1      #start variables

def pair_check(letter1,letter2): #check two consecutive letters
    global pairs
    if letter2==(len(message)-1):
        if message[letter1]==message[letter2]:
            pairs+=1
        else:
            return False
    elif message[letter1]==message[letter2]:
        pairs+=1
        return pair_check(letter1+2,letter2+2)
    else:
        return pair_check(letter1+2,letter2+2)
        
pair_check(letter1,letter2)
print('Number of pairs:',pairs)

    