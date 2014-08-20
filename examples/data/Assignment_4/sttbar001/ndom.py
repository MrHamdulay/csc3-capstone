def ndom_to_decimal (a):
    x=0
    a = str(a)
    length = len(str(a))
    if length == 3:
        num1 = int(a[0:1])
        num2 = int(a[1:2])
        num3 = int(a[2:])
        x = num1*(36)+num2*(6)+ num3
    elif length == 2:
        x = int(a[0:1])*(6)+int(a[1:2])
    elif length==1:
        x = int(a[0:1])
    return (x)
def decimal_to_ndom (a):
    length = len(str(a))
    x = ""
    for i in range(length):
        re = a%6
        new = int(a/6)
        x = str(re)+x
        a = new
    x =str(new)+x
    if x[:1] =="0":
        x = x[1:]
    return(x)          
    

def ndom_add (a, b):
    num1 = ndom_to_decimal (a)
    num2 = ndom_to_decimal (b)
    num3 =num1+num2
    q= decimal_to_ndom (num3)
    return(q)     
        
def ndom_multiply (a, b):
    num1 = ndom_to_decimal (a)
    num2 = ndom_to_decimal (b) 
    num3 = num1*num2
    q = decimal_to_ndom (num3)
    return(q)