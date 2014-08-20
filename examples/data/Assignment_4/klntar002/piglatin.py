def toPigLatin(s):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    u=''
    q=''
    a=s.split()
    for i in (a):
        if i[0] in vowels:
                u=u+(i+'way ')
        elif i[0] not in vowels:
            q=""
            for k in i:
                if k not in vowels:
                    
                    q=q+k
                    
                elif k in vowels:
                    break
            
            u=u+((i[len(q):])+'a'+q+'ay ')
               
    return(u)        
if __name__=='__main':            
    toPigLatin('easy game thorn')   
    
    
    
     
def toEnglish(s):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    t=''
    
    a=s.split()
    for i in (a):
        if i[0] in vowels and i[-1]+i[-2]+i[-3]==('yaw'):
            t=t+((i[0:(len(i)-3)]))+' '
            
        elif i[-1]+i[-2]==('ya'):
            i=i[0:(len(i)-2)] #the new i
            
            err=''
            
            for k in i[::-1]:
                
                if k not in vowels:
                    
                    err=err+k
                    
                elif k==('a'):
                    break
            t=t+(err[::-1]+(i[:(len(i)-(len(err)+1))]))+' '
           
    return(t)      
                 
if __name__=='__main':                  
    toEnglish(s)                      
            
            
            
           
            