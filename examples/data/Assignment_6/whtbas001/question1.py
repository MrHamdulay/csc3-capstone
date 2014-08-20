#CSC1015F 
#ASSIGNMENT 6
#QUESTION 1
#WHTBAS001
#23/04/2014

def max_len(x):
    maxlength = len(x[0]) #defines first string to be longest
    for i in range(1, len(x)):
        if len(x[i]) >= maxlength:
            maxlength = len(x[i]) #redefines var of max if current string in loop is longer than previous entries
    return maxlength #returns the number of characters in longest string

def justification(y): #as format wont let me input a var for characters...
    chars = max_len(names) #calls max_length script and saves as a var
    for i in range(len(y)): #loops through list
        spaces = (chars - len(y[i])) #calculates front spaces needed
        print(" "*spaces,y[i],sep="") #prints with spaces included
    

names = list()
name = input('Enter strings (end with DONE):\n') # initalize before the loop
while name != 'DONE':           # while NOT DONE
    names.append(name) #adds the new string
    name = input('')  #resets loop
print()
print("Right-aligned list:")
if names != []: #in case of empty list...
    justification(names)
