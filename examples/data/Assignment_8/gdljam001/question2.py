"""James Godlonton
Counting number of pairs
04 May 2014"""

def main():
    """Main function for input output and calling recursive formula"""
    print("Enter a message:")
    checkStr=input("")
    print("Number of pairs: "+str(checkPs(checkStr,0,0)))
    
    
def checkPs(strN,pos,count):
    """a recursive formula to count the number of pairs in a string"""
    if pos >=len(strN)-1:
        #Recursive termination if reach the end of the string, return the value of count
        
        return count
    
    elif strN[pos]==strN[pos+1]:
        #If two letters are a pair add one to count and 2 to position (so that overlapping pairs dont count)
        pos=pos+2
        count=checkPs(strN,pos,count+1)
        
    else:
        #If not a pair go to next letter and try again 
        pos=pos+1
        count=checkPs(strN,pos,count)
    #Once recursion to count pairs is done return the count
    return count

    
if __name__=="__main__":
    main()
        
    