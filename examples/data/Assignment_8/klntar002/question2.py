# tarisai kalinde
# klntar002
# a program to count number of pairs of repeating char in a string using a recusive function and no loop of any kind

string=input('Enter a message:\n')
string=string.replace(",","")
comma=','.join(string) # joins all characters by a comma
chars=comma.split(',')    # splits all characters by the comma to make a list of letters in the string
counter=0 # counting number of pairs
def countit(chars,counter):
   # base case
    if len(chars)<2:
        return 'Number of pairs: '+ str(counter)  
    else:
        
        if chars[0]==chars[1]: 
            #global counter
            counter+=1 # counter accumulation
            
            return countit(chars[2:],counter) # recursive function
        else:
            return countit(chars[1:],counter)
    

print(countit(chars,counter))
    
    

    
    