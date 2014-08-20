# Ndom module
# badugela mulisa
# 2 April 2014

def ndom_to_decimal (a):
    answer=0
    a=str(a)
    exp=len(a)
    for i in a:
        exp=exp-1
        i=int(i)
        answer=answer+(i*(6**exp))      
    return(answer)
        
def decimal_to_ndom (a):
    quotient=a
    answer=""
    while quotient !=0:
        remainder = quotient%6
        quotient =quotient//6
        remainder=str(remainder)
        answer+=remainder
       
    return(answer[::-1])    

def ndom_add (a,b):
    answera=0
    
    a=str(a)
    exp=len(a)
    for i in a:
        exp=exp-1
        i=int(i)
        answera +=(i*(6**exp))
            
    answerb=0
    b=str(b)
    exp=len(b)
    for i in b:
        exp=exp-1
        i=int(i)
        answerb +=(i*(6**exp))
        
    answer = answera +answerb
       
    quotient = answer
    newanswer=""
    while quotient !=0:
        remainder = quotient%6
        quotient =quotient//6
        remainder=str(remainder)
        newanswer+=remainder
    return(newanswer[::-1])

def ndom_multiply (a, b):
    
    answera=0
    a=str(a)
    exp=len(a)
    for i in a:
        exp=exp-1
        i=int(i)
        answera =answera+(i*(6**exp))
            
    answerb=0
    b=str(b)
    exp=len(b)
    for i in b:
        exp=exp-1
        i=int(i)
        answerb =answerb+(i*(6**exp))
        
    answer = answera *answerb
       
    quotient=answer
    newanswer=""
    while quotient !=0:
        remainder = quotient%6
        quotient =quotient//6
        remainder=str(remainder)
        newanswer+=remainder
    return(newanswer[::-1])        