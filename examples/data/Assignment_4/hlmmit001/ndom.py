def ndom_to_decimal(a):
    if len(str(a))==1:
        if eval(str(a)[0])>=6:
            print("invalid input")
        else:
            calc_1=a
            
            return calc_1
    if len(str(a))==2:
        if eval(str(a)[0])>=6 or eval(str(a)[1])>=6:
            print("invalid input")
        else:
            calc_1=(eval(str(a)[0])*6)
            calc_2=calc_1+(eval(str(a)[1]))  
            
            return calc_2
    if len(str(a))==3:
        if eval(str(a)[0])>=6 or eval(str(a)[1])>=6 or eval(str(a)[2])>=6:
            print("invalid input")
        else:
            calc_1=(eval(str(a)[0])*6)
            calc_2=calc_1+(eval(str(a)[1]))
            calc_3=calc_2*(6)
            calc_4=calc_3+eval(str(a)[2])
            
            return calc_4

def decimal_to_ndom(a):
    if len(str(a))==1:
        calc_1=a
         
        return calc_1
    if len(str(a))==2:
        calc_1=a%6
        calc_2=(a//6)%6
        calc_3=((a//6)//6)%6
        if calc_3!=0:
            
            return (eval(str(calc_3)+str(calc_2)+ str(calc_1)))
        if calc_3==0:
            
            return (eval(str(calc_2)+ str(calc_1)))
    if len(str(a))==3:
        calc_1=a%6
        calc_2=(a//6)%6
        calc_3=((a//6)//6)%6
        calc_4=((a//6)//6//6)%6
        if calc_4!=0:
            
            return (eval(str(calc_4) + str(calc_3) + str(calc_2) + str(calc_1)))
        if calc_4==0:
            
            return (eval(str(calc_3)+ str(calc_2) + str(calc_1)))
 
 
def ndom_add(a, b):
    add=(ndom_to_decimal(a)+ ndom_to_decimal(b))
    ans=decimal_to_ndom(add)
    return ans
    
def ndom_multiply(a, b):
    a= ndom_to_decimal(a)
    b= ndom_to_decimal(b)
    multiply=(a*b)
    ans=decimal_to_ndom(multiply)
    return ans
    

    

    