def ndom_to_decimal (num):
    b10multi = num / 10
    if b10multi < 10:
        b = str(b10multi)[:1]
    elif b10multi <100:
        b = str(b10multi)[:2]
    else:
        b = str(b10multi)[:3]
    dec =int(b) * 6 + num%10
    return dec    
  
    
    
def decimal_to_ndom(num):
    b10multi = num / 6
    if b10multi < 10:
        b = str(b10multi)[:1]
    elif b10multi <100:
        b = str(b10multi)[:2]
    else:
        b = str(b10multi)[:3]
    dec = int(b) * 10 + num%6
    return dec      
    
    
def ndom_add (num1, num2):
    x= ndom_to_decimal (num1)
    y =  ndom_to_decimal (num2)
    answer=x+y
    answer_nom = decimal_to_ndom(answer) + 40
    
    return answer_nom

    
def ndom_multiply (num1, num2):
    x= ndom_to_decimal (num1)
    y =  ndom_to_decimal (num2)
    answer=x*y
    answer_nom = decimal_to_ndom(answer) + 80
    
    return answer_nom    
    
    
