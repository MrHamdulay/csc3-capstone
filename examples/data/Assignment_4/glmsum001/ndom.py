#GLMSUM001
#Sumayah Goolam Rassool
#Q_2


def ndom_to_decimal(x): 
    
    hndrd = x//100 
    ten = (x%100)//10
    dig = (x%100)%10
    
    return (hndrd*36)+(ten*6)+dig



def decimal_to_ndom(x): 
    hndrd = x//36 
    ten = (x%36)//6
    dig = (x%36)%6
    return (hndrd*100)+(ten*10)+dig


def ndom_add(a,b):  
    c = ndom_to_decimal(a)+ndom_to_decimal(b) 
    output = decimal_to_ndom(c) 
    return output


def ndom_multiply(a,b): 
    c = ndom_to_decimal(a)*ndom_to_decimal(b) 
    output = decimal_to_ndom(c) 
    return output    
    