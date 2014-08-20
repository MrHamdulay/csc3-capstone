#a program to count the numer of pairs in a string
#F.J.Chigwaza
#08 May 2014

msg= input('Enter a message:\n')
pair_count=0
def pair_counter(msg,pair_count):
    
    
    m=str(msg)
    n=m.split(" ")
    
    

#base case
    
    if len(m)<2:
        return 'Number of pairs: '+str(pair_count)

#recursive step

    elif m[0]==m[1]:
        #global pair_count
        pair_count+=1
        
        return pair_counter(m[2:],pair_count)
    
    else:
        return pair_counter(m[1:],pair_count)
                              
#output
print(pair_counter(msg,pair_count))
    
        
    
