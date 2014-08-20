m = input("Enter a message:\n")

def count(m):
    
    if m =="" or m==" ":# base case 
        return 0
    elif (len(m))==1:# if length =1 there cannot be any pairs
        return 0
    
    else:
        if m[0]==m[1]:
            m=m[2:] #if letter are the same it trancates the first and call   the fuction again
            return 1 + count(m)
        else:
            return count(m[1:])
        
count=count(m)
print("Number of pairs: " +str(count))

            
        
        
        
        
        
    