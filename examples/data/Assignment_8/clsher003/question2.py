"""program to count number of pairs of characters in a string
herman claassens
4 may 2014"""

string=input('Enter a message:\n')  
count=0

def repeat(string,count):        # use parameter count to count number of pairs
    #string=string.lower()
    if string=='':              # if the message is empty: no pairs
        return 0
    if len(string)==1:          # continue recursion until their is only one value left in the string
        return count
    if string[0]==string[1]:    # check if the current character is equall to the next character
        count+=1           # if it is equal, add one to the count parameter
    return repeat(string[1:],count) 

 
    
print('Number of pairs:', repeat(string,count))