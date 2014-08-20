"""checking for pairs
Richard Marais
09/05/14"""

string = input('Enter a message:\n')   #input

def PairChecker(string,count,pairs):    #function including variables for the input, counter and output
    if count == len(string)-1:
        print('Number of pairs:',pairs)             #base case
    elif string[count] == string [count+1] and count == len(string)-2:      #if two adjacent letters are the same at the end
        pairs+=1
        print('Number of pairs:',pairs)        
    elif string[count] == string [count+1]:          #if two adjacent letters are the same increase the pairs value
        pairs+=1
        PairChecker(string,count+2,pairs)
    else:                                     #if they arent, run again for the next set of values
        PairChecker(string,count+1,pairs)

PairChecker(string,0,0)
