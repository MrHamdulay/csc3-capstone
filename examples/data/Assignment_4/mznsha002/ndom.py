#2 April 2014
#Shaun Muzenda
#Converting from Ndom to decimal numbers or vice a versa

def ndom_to_decimal (a):
    a = str(a)
    to_Dec=len(a)
    count = 0
    for i in (a):
        to_Dec = to_Dec - 1
        i = int(i)
        count = count + (i * (6**to_Dec))      
    return(count)    

def decimal_to_ndom (a):
    count = ""
    divider = a
    while divider != 0:
        remainder = divider % 6
        divider = divider // 6
        remainder = str(remainder)
        count = count + remainder     
    return(count[::-1])  


def ndom_add (a,b):

    count_A = 0
    a = str(a)
    num = len(a)
    for i in (a):
        num = num - 1
        i = int(i)
        count_A = count_A + (i*(6**num))
        
            
    count_B = 0
    b = str(b)
    num = len(b)
    for i in (b):
        num = num - 1
        i = int(i)
        count_B = count_B + (i*(6**num))
        
        
    total = count_A + count_B    
    divider =total
    total_2 = ""
    while divider != 0:
        remainder = divider % 6
        divider = divider // 6
        remainder = str(remainder)
        total_2 = total_2 + remainder
    return(total_2[::-1])

def ndom_multiply (a, b):
    
    count_A=0
    a = str(a)
    num = len(a)
    for i in (a):
        num = num - 1
        i = int(i)
        count_A = count_A + (i*(6**num))
            
    count_B = 0
    b = str(b)
    num = len(b)
    for i in b:
        num = num-1
        i = int(i)
        count_B = count_B + (i*(6**num))
        
    total = count_A * count_B
       
    divider = total
    total_2 = ""
    while divider != 0:
        remainder = divider % 6
        divider = divider // 6
        remainder = str(remainder)
        total_2 = total_2 + remainder
    return(total_2[::-1])        