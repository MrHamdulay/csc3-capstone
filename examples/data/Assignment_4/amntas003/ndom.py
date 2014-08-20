def ndom_to_decimal(x):
    x = str(x)
    if len(x)==1:
        x = int(x)
        return x
    elif len(x)==2:
        digits = x[1]
        digits = int(digits)
        tens = x[0]
        tens = int(tens)
        y = digits*1 + tens*6
        return y
    elif len(x)==3:
        digits = x[2]
        digits = int(digits)
        tens = x[1] 
        tens = int(tens)
        hundreds = x[0]
        hundreds = int(hundreds)
        y = digits*1 + tens*6 + hundreds*36
        return y
        
def decimal_to_ndom(x):
    hundreds = x//36
    tens = (x-hundreds*36)//6
    digits = (x - hundreds*36 - tens*6)//1
    y = hundreds*100 +tens*10 + digits
    return y
       
def ndom_add(x,y):
    x = str(x)
    if len(x)==1:
        x = int(x)
    elif len(x)==2:
        digits = x[1]
        digits = int(digits)
        tens = x[0]
        tens = int(tens)
        x = digits*1 + tens*6
    elif len(x)==3:
        digits = x[2]
        digits = int(digits)
        tens = x[1] 
        tens = int(tens)
        hundreds = x[0]
        hundreds = int(hundreds)
        x = digits*1 + tens*6 + hundreds*36

    
    y = str(y)
    if len(y)==1:
        y = int(y)
    elif len(y)==2:
        digits = y[1]
        digits = int(digits)
        tens = y[0]
        tens = int(tens)
        y = digits*1 + tens*6
    elif len(y)==3:
        digits = y[2]
        digits = int(digits)
        tens = y[1] 
        tens = int(tens)
        hundreds = y[0]
        hundreds = int(hundreds)
        y = digits*1 + tens*6 + hundreds*36

    z = x + y
    
    hundreds = z//36
    tens = (z - hundreds*36)//6
    digits = (z - hundreds*36 - tens*6)//1
    z = hundreds*100 +tens*10 + digits  
    
    return z
 
def ndom_multiply(x,y):
    
    x = str(x)
    if len(x)==1:
        x = int(x)
    elif len(x)==2:
        digits = x[1]
        digits = int(digits)
        tens = x[0]
        tens = int(tens)
        x = digits*1 + tens*6
    elif len(x)==3:
        digits = x[2]
        digits = int(digits)
        tens = x[1] 
        tens = int(tens)
        hundreds = a[0]
        hundreds = int(hundreds)
        x = digits*1 + tens*6 + hundreds*36
    
    y = str(y)
    if len(y)==1:
        y = int(y)
    elif len(y)==2:
        digits = y[1]
        digits = int(digits)
        tens = y[0]
        tens = int(tens)
        y = digits*1 + tens*6
    elif len(y)==3:
        digits = y[2]
        digits = int(digits)
        tens = y[1] 
        tens = int(tens)
        hundreds = y[0]
        hundreds = int(hundreds)
        y = digits*1 + tens*6 + hundreds*36
    
    z = x*y

    hundreds = z//36
    tens = (z - hundreds*36)//6
    digits = (z - hundreds*36 - tens*6)//1
    z = hundreds*100 +tens*10 + digits  
    
    return z