#Program to count pairs in a string
#Kayla Hendricks
#08 May 2014
count=0

def count_pairs(mess):
    global count
    if len(mess)==1:    #if string consists of one letter, there are no pairs.
        count=count
    elif len(mess)==2 and mess[0]==mess[1]: #if the string consists of two letters and they equal one another
        count+=1 #add one to number of pairs
    elif mess[0]!=mess[1]:      #else if first and second letter not equal, start from the beginning with the string less it's first letter
        return count_pairs(mess[1:])
    else:
        count+=1                #else if they are equal, add one to the count
        return count_pairs(mess[2:])
mess=input("Enter a message:\n")    
count_pairs(mess)
print("Number of pairs:",count)
    
        

        
        
    

            
        
    
        
            