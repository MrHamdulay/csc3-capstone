# 09/05/2014 
# SCHCH027
# Question1

string=input("Enter a message:\n")
counter=0
paircounter=0
#recursive function counts non-overlapping pairs
def count_pairs(string,counter,paircounter,dontCount):
    length=len(string)
    
    if counter<length and counter+1!=length:
        
        if string[counter]==string[counter+1] and dontCount==False:
            paircounter+=1
            counter+=1
            dontCount=True
            count_pairs(string,counter,paircounter,dontCount)
            # don't count skips the next possible pair if last two characters were a pair
            
        else:
            counter+=1
            dontCount=False
            count_pairs(string,counter,paircounter,dontCount)
        
    else:
        print("Number of pairs:", paircounter )
dontCount=False

count_pairs(string,counter,paircounter,dontCount)
