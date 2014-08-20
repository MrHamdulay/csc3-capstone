""" count the number of pairs of repeating charactors
Roger Cox 
8/05/2014"""

def pair_counter(string) :

    if len(string) >= 2  :
        #print(string)
    
        if string[0]==string[1] :
            #print(string[0])
            
            return (1+ pair_counter(string[2:]))# so as not to pick up mmm as two pairs
        
        else :
            return (pair_counter(string[1:]))
    else:
        return 0 
    
    
    
    
    
    
    
    
string=input("Enter a message:\n")    
print("Number of pairs:",pair_counter(string))
