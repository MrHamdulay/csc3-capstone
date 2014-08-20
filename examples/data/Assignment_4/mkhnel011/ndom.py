# nelisile mkhwebane
# question 2

#decimal_ndom

def decimal_to_ndom(a):
    sum_r=""
    while a!=0:
        sum_r=str(a%6) + sum_r
        a=a//6
    return eval(sum_r)
#decimal_to_ndom(20)

def ndom_to_decimal(a):
    a=str(a)
    if len(a)==1:
        units=a[0]
        tens='0'
        hundreds='0'
    
    elif (len(a)==2):
        units=a[0]
        tens=a[1]
        hundreds='0'
        
    elif len(a)==3:
        units=a[0]
        tens=a[1]
        hundreds=a[2]
    
    baseU=1*(eval(units))
    baseT=10*(eval(tens))
    baseH=100*(eval(hundreds))
    
    decimal= baseU + baseT + baseH
    return (decimal)
    
#ndom_to_decimal(32)

def ndom_add(a,b):
    a=str(a)
    b=str(b)
    if len(a)==1:
        unitsA=a[0]
        tensA='0'
        hundredsA='0'
    elif len(a)==2:
        unitsA = a[1]
        tensA = a[0]
        hundredsA = '0'     
    elif len(a)==3:
        unitsA=(a[2])
        tensA=(a[1])
        hundredsA=(a[0])
    
    if len(b)==1:
        unitsB=a[0]
        tensB='0'
        hundredsB='0'
    elif len(b)==2:
        unitsB= a[0]
        tensB = a[1]
        hundredsB = '0'     
    elif len(b)==3:
        unitsB=b[0]
        tensB=b[1]
        hundredsB=b[2]
    
    sum_base_units=(eval(unitsA)+eval(unitsB))*1
    sum_base_tens=(eval(tensB)+eval(tensB))*10
    sum_base_hundreds=(eval(hundredsA)+eval(hundredsB))*100
    return (sum_base_units + sum_base_tens + sum_base_hundreds)

def ndom_multiply(a,b):
    a=str(a)
    b=str(b)
    if len(a)==1:
        unitsA=a[0]
        tensA='0'
        hundredsA='0'
    elif len(a)==2:
        unitsA = a[1]
        tensA = a[0]
        hundredsA = '0'     
    elif len(a)==3:
        unitsA=(a[2])
        tensA=(a[1])
        hundredsA=(a[0])
        
    if len(b)==1:
        unitsB=a[0]
        tensB='0'
        hundredsB='0'
    elif len(b)==2:
        unitsB= a[0]
        tensB = a[1]
        hundredsB = '0'     
    elif len(b)==3:
        unitsB=b[0]
        tensB=b[1]
        hundredsB=b[2]
        
    product_units = (eval(unitsA)*eval(unitsB))*1
    product_tens=(eval(tensA)*eval(tensB))*10
    product_hundreds=(eval(hundredsA)*eval(hundredsB))*100
    return (product_units +product_tens +product_hundreds)

    