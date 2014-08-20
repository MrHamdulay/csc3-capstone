# Ndom 
# BDLREN001
# Budeli Rendani
# 30 March 2014

def ndom_to_decimal (a): # ndom_to_decimal
    
    answer=0
    
    a=str(a)
    
    exp=len(a)
    
    for j in a:
        
        exp=exp-1
        
        j=int(j)
        
        answer=answer+(j*(6**exp))      
    
    return(answer)
        
def decimal_to_ndom (a): # deciaml_to_ndom
    
    quotient=a
    
    answer=""
    
    while quotient !=0:
        
        remainder = quotient%6
        
        quotient =quotient//6
        
        remainder=str(remainder)
        
        answer+=remainder
       
    return(answer[::-1])    

def ndom_add (a,b): # ndom add
    
    answera=0
    
    
    a=str(a)
    
    exp=len(a)
    
    for j in a:
        
        exp=exp-1
        
        j=int(j)
        
        answera +=(j*(6**exp))
            
    answerb=0
   
    b=str(b)
    
    exp=len(b)
    
    for j in b:
        
        exp=exp-1
        
        j=int(j)
        
        answerb +=(j*(6**exp))
        
    answer = answera +answerb
       
    quotient = answer
    
    newanswer=""
    
    while quotient !=0:
        
        remainder = quotient%6
        
        quotient =quotient//6
        
        remainder=str(remainder)
        
        newanswer+=remainder
    
    return(newanswer[::-1])

def ndom_multiply (a, b): # ndom multiply 
    
    answera=0
    
    a=str(a)
    
    exp=len(a)
    
    for j in a:
        
        exp=exp-1
        
        j=int(j)
        
        answera =answera+(j*(6**exp))
            
    answerb=0
    
    b=str(b)
    
    exp=len(b)
    
    for j in b:
        
        exp=exp-1
        
        j=int(j)
        
        answerb =answerb+(j*(6**exp))
        
    answer = answera *answerb
       
    quotient=answer
    
    newanswer=""
    
    while quotient !=0:
        
        remainder = quotient%6
        
        quotient =quotient//6
        
        remainder=str(remainder)
        
        newanswer+=remainder
    
    return(newanswer[::-1])        