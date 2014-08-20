def ndom_to_decimal (x):
    num = 0
    z = str(x)
    exp = len(z)
    for i in z:
        exp =exp- 1
        i = int(i)
        num = num + i*(6**exp)      
    return num
        
def decimal_to_ndom (x):
    q = x
    temp = ""
    while q != 0:
        remainder = q % 6
        q//=6
        remainderST = str(remainder)
        temp+= remainderST
       
    return temp[::-1]     

def ndom_add (x,y):

    temp=0
    x=str(x)
    exp=len(x)
    for x in x:
        exp=exp-1
        x=int(x)
        temp = temp + (x*(6**exp))
            
    temp2=0
    y=str(y)
    exp=len(y)
    for x in y:
        exp-=1
        x=int(x)
        temp2 = temp2 + (x*(6**exp))
        
    t = temp + temp2
       
    q = t
    new =""
    while q !=0:
        remainder = q%6
        q =q//6
        remainderST=str(remainder)
        new += remainderST
    return new[::-1]

def ndom_multiply (x, y):
    
    temp=0
    x=str(x)
    exp=len(x)
    for x in x:
        exp=exp-1
        x=int(x)
        temp =temp+(x*(6**exp))
            
    temp2=0
    y=str(y)
    exp=len(y)
    for x in y:
        exp-=1
        x=int(x)
        temp2 =temp2+(x*(6**exp))
        
    temp = temp *temp2
       
    q =temp
    new=""
    while q !=0:
        remainder = q%6
        q =q//6
        remainderST=str(remainder)
        new+= remainderST
    return new[::-1]      
    