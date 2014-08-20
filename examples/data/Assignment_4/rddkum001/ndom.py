def ndom_to_decimal(a):
    hundred=a//100
    ten=(a//10)%10
    unit=a%10
    d= (hundred*36)+(ten*6)+unit
    
    return d

def decimal_to_ndom (a):
    fig1=a//36
    fig1a=a%36
    fig2=fig1a//6
    fig2a=fig1a%6
    
    n= (100*fig1)+(10*fig2)+fig2a
    
    return n

def ndom_add (a, b):
    hundredA=a//100
    tenA=(a//10)%10
    unitA=a%10  
    
    hundredB=b//100
    tenB=(b//10)%10
    unitB=b%10     
    
    unitSum=decimal_to_ndom(unitA+unitB)
    #unitCarry=unitSum//10
    #unitStay= unitSum%10
    
    tenSum= (decimal_to_ndom(tenA+tenB))*10
    #tenCarry= tenSum//10
    #tenStay=tenSum%10
    
    hundredSum= (decimal_to_ndom(hundredA+hundredB))*100
    
    total=hundredSum+tenSum+unitSum
    return total

def ndom_multiply(a,b):
    ad= ndom_to_decimal(a)
    bd=ndom_to_decimal(b)
    prod= ad*bd
    prodN= decimal_to_ndom(prod)

    return prodN
    
    