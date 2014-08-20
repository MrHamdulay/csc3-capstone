"""Shriya Roy
8 May 2014
counting program"""
def pair(n,i):
    
    
    if len(n)==0:#checks if length is 0
        
        return print("Number of pairs:",i)
    if len(n)==1:#checks if length is 1
        return  print("Number of pairs:",i)
    else:
        if n[0]==n[1]:#checks if the first two are identical
            i+=1
            return pair(n[2:],i)#increasing increments of 2
            
        else:
            return pair(n[2:],i)

        
        
        
n=input("Enter a message:\n")
pair(n,0)
                    
        
        
                    
    
    
    
    
    
    
    



