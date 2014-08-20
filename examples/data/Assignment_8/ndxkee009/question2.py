"""Keegan Naidoo
NDXKEE009
4 May 2014"""

text=input("Enter a message:\n")         #Inputs message

def Pairs(text):
    
    if text=="":                         #Base cases if empty string or only 1 character is inputted return 0
        return 0
    elif(len(text)==1):
        return 0
    
    else:
        
        if text[0]==text[1]:                     #If first letter = 2nd letter return 1 pair and move on to next pair of letters
            text=text[2:]
            return 1+Pairs(text)
        else:
            return Pairs(text[1:])           #Otherwise just move on to next pair of letters
        
No_of_pairs=Pairs(text)
print("Number of pairs: " +str(No_of_pairs))   #Prints the pairs of letters