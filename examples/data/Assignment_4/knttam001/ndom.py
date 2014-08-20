def ndom_to_decimal(a):
    a = str(a)
    if len(a)==1:
        a = int(a)
        return a
    elif len(a)==2:
        digits = a[1]
        digits = int(digits)
        tens = a[0]
        tens = int(tens)
        b = digits*1 + tens*6
        return b
    elif len(a)==3:
        digits = a[2]
        digits = int(digits)
        tens = a[1] 
        tens = int(tens)
        hundreds = a[0]
        hundreds = int(hundreds)
        b = digits*1 + tens*6 + hundreds*36
        return b
    elif len(a)==4:
        digits = a[3]
        digits = int(digits)
        tens = a[2] 
        tens = int(tens)
        hundreds = a[1]
        hundreds = int(hundreds)
        thousands = a[0]
        thousands = int(thousands)
        b = digits*1 + tens*6 + hundreds*36 + thousands*216
        return b 
        
def decimal_to_ndom(a):
    thousands = a//216
    hundreds = (a - thousands*216)//36
    tens = (a - thousands*216 - hundreds*36)//6
    digits = (a - thousands*216 - hundreds*36 - tens*6)//1
    b = thousands*1000 + hundreds*100 +tens*10 + digits
    return b
       
def ndom_add(a,b):
    
    # make a a decimal
    a = str(a)
    if len(a)==1:
        a = int(a)
    elif len(a)==2:
        digits = a[1]
        digits = int(digits)
        tens = a[0]
        tens = int(tens)
        a = digits*1 + tens*6
    elif len(a)==3:
        digits = a[2]
        digits = int(digits)
        tens = a[1] 
        tens = int(tens)
        hundreds = a[0]
        hundreds = int(hundreds)
        a = digits*1 + tens*6 + hundreds*36
    elif len(a)==4:
        digits = a[3]
        digits = int(digits)
        tens = a[2] 
        tens = int(tens)
        hundreds = a[1]
        hundreds = int(hundreds)
        thousands = a[0]
        thousands = int(thousands)
        a = digits*1 + tens*6 + hundreds*36 + thousands*216
    
    # make b a decimal
    b = str(b)
    if len(b)==1:
        b = int(b)
    elif len(b)==2:
        digits = b[1]
        digits = int(digits)
        tens = b[0]
        tens = int(tens)
        b = digits*1 + tens*6
    elif len(b)==3:
        digits = b[2]
        digits = int(digits)
        tens = b[1] 
        tens = int(tens)
        hundreds = b[0]
        hundreds = int(hundreds)
        b = digits*1 + tens*6 + hundreds*36
    elif len(b)==4:
        digits = b[3]
        digits = int(digits)
        tens = b[2] 
        tens = int(tens)
        hundreds = b[1]
        hundreds = int(hundreds)
        thousands = b[0]
        thousands = int(thousands)
        b = digits*1 + tens*6 + hundreds*36 + thousands*216
    
    c = a + b
    
    # make c a ndom
    thousands = c//216
    hundreds = (c - thousands*216)//36
    tens = (c - thousands*216 - hundreds*36)//6
    digits = (c - thousands*216 - hundreds*36 - tens*6)//1
    c = thousands*1000 + hundreds*100 +tens*10 + digits  
    
    return c
 
def ndom_multiply(a,b):
    
    # make a a decimal
    a = str(a)
    if len(a)==1:
        a = int(a)
    elif len(a)==2:
        digits = a[1]
        digits = int(digits)
        tens = a[0]
        tens = int(tens)
        a = digits*1 + tens*6
    elif len(a)==3:
        digits = a[2]
        digits = int(digits)
        tens = a[1] 
        tens = int(tens)
        hundreds = a[0]
        hundreds = int(hundreds)
        a = digits*1 + tens*6 + hundreds*36
    elif len(a)==4:
        digits = a[3]
        digits = int(digits)
        tens = a[2] 
        tens = int(tens)
        hundreds = a[1]
        hundreds = int(hundreds)
        thousands = a[0]
        thousands = int(thousands)
        a = digits*1 + tens*6 + hundreds*36 + thousands*216
    
    # make b a decimal
    b = str(b)
    if len(b)==1:
        b = int(b)
    elif len(b)==2:
        digits = b[1]
        digits = int(digits)
        tens = b[0]
        tens = int(tens)
        b = digits*1 + tens*6
    elif len(b)==3:
        digits = b[2]
        digits = int(digits)
        tens = b[1] 
        tens = int(tens)
        hundreds = b[0]
        hundreds = int(hundreds)
        b = digits*1 + tens*6 + hundreds*36
    elif len(b)==4:
        digits = b[3]
        digits = int(digits)
        tens = b[2] 
        tens = int(tens)
        hundreds = b[1]
        hundreds = int(hundreds)
        thousands = b[0]
        thousands = int(thousands)
        b = digits*1 + tens*6 + hundreds*36 + thousands*216
    
    c = a*b
    
    # make c a ndom
    thousands = c//216
    hundreds = (c - thousands*216)//36
    tens = (c - thousands*216 - hundreds*36)//6
    digits = (c - thousands*216 - hundreds*36 - tens*6)//1
    c = thousands*1000 + hundreds*100 +tens*10 + digits  
    
    return c  