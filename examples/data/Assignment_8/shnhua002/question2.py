"""Pairs Counter
Charlie Shang
8 May 2014"""

#Input string to be processed
string = input("Enter a message:\n")

#count for pairs
cnt = 0

def count_pairs(string):
    global cnt
    
    #end the recursion once string length <= 1
    if 1 >= len(string):
        print("Number of pairs:", cnt)
              
    elif string[0] == string[1]: #If first 2 characters are the same, delete and add 1 to cnt. 
        cnt += 1
        string = string[2:]
        return count_pairs(string)
        
    else: #If first 2 characters are unequal, only delete the first character.  
        string = string[1:]
        return count_pairs(string)
    
if __name__=="__main__":
    count_pairs(string)
    
                            