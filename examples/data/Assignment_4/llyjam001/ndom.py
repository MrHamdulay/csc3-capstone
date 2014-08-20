def ndom_to_decimal(a):
    a=str(a)
    
    if len(a)==1:
        answer=a
        
    elif len(a)==2:
        zero=eval(a[-1])
        one=eval(a[-2])
        one=one*6
        answer=zero+one
        
    elif len(a)==3:
        zero=eval(a[-1])
        one=eval(a[-2])        
        two=eval(a[-3])
        one=one*6
        two=two*36
        answer=zero+one+two
    
    return answer  


    
def decimal_to_ndom(a):
    if a>=36:
        two=str(a//36)
        remainder_one=a%36
        one=str(remainder_one//6)
        remainder_two=remainder_one%6
        zero=str(remainder_two)
        answer=two+one+zero
        return answer
    elif a>6:
        one=str(a//6)
        remainder=a%6
        zero=str(remainder)
        answer=one+zero
        return answer       
    else:
        answer=a
        return answer
    
def ndom_add(a,b):
    A=ndom_to_decimal(a)
    B=ndom_to_decimal(b)
    added=A+B
    answer=decimal_to_ndom(added)
    return answer
    
def ndom_multiply(a,b):
    A=ndom_to_decimal(a)
    B=ndom_to_decimal(b)
    multiplied=A*B
    answer=decimal_to_ndom(multiplied)
    answer=eval(answer)
    return answer 
    
    