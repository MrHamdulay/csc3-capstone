#Counts numbers of pairs of repeated letters in a string
#Jennifer Yuan
#7 May 2014

s = input('Enter a message: \n') #ask for sentence from user 

def pairs(s):
    if len(s) < 2: #makes sure that index is in range
        return 0
    elif s[0] == s[1]: #checks if two identical letters are next to each  other
        return 1+pairs(s[2:]) #if they are, it skips those two letters and goes to look at the next two letters
    else: 
        return 0+pairs(s[1:]) #if they arent, it skips that letter and goes to look at the next two letters
    
print('Number of pairs:', pairs(s)) #prints the number of pairs

