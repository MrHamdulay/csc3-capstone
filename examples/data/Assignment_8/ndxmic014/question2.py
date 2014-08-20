#NDXMIC014
#8 MAY 2014
#ASSIGNMENT 8
#QUESTION TWO

#Finds pairs of alphabhets in words
ct=0
def county(wd):
    global ct
    if wd=='':
        return ct
    else:
        
        if(len(wd)>1 and wd[0]==wd[1]):
    
            ct=ct+1
        
            return county(wd[2:len(wd)])
        else:
            return county(wd[1:len(wd)])

z=input("Enter a message:\n")         #asks user for an input
print("Number of pairs:",county(z))