


factor = 2

def prime_number(n):
    global factor
    if (n % factor == 0 and n>factor):
        return False
    elif(n > factor):
        factor+= 1
        return prime_number(n)
    

incr=0
life=600

def count(answer):
    global incr
    incr=answer
    global life
    global sq_r
    
    if incr==life:
        print('Done')
    elif incr< life:
        
        incr+=1
        string=str(incr)
        number=prime_number(incr)
        
        if ((string)==(string[::-1])):
            number=prime_number(incr)
            if (number is False):
                print(incr,'False')
                return count(incr)
            else:
                print(incr)
                return count(incr)
        else:
            return count(incr)

count(200)    
    

    
            

                     
    
        
        
    
    
        
                                                          
                         
    