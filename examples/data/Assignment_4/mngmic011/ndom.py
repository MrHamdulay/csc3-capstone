#question2
#Micaela Menegaldo

def decimal_to_ndom (a):
    div=a//6
    rem=a%6
    if div>=6:
        place3=div//6
        rem2=div%6     
        result=(str(place3)+str(rem2)+str(rem))
    else:
        result=(str(div)+str(rem))
    return result

def ndom_to_decimal (a):
    num=str(a)
    if len(num)==3:
        thirdplace=num[0:1]
        decimal3=int(thirdplace)*36
        secondplace=num[1:2]
        decimal2=int(secondplace)*6
        firstplace=int(num[2:3])
        result=(decimal3+decimal2+firstplace)
    elif len(num)==2:
        secondplace=num[0:1]
        decimal2=int(secondplace)*6
        firstplace=int(num[1:2])
        result=(decimal2+firstplace) 
    elif len(num)==1:
        firstplace=int(num[0:1])
        result=(firstplace)        
    return result
    
def ndom_add (a,b):
    a=str(a)
    b=str(b)
    a="{0:0>3}".format(a)
    b="{0:0>3}".format(b)
    position3=int(a[(len(a)-1):len(a)])+int(b[(len(b)-1):len(b)])
    extra_pos2=0
    if position3>5:
        extra_pos2=position3//6
        position3=position3%6
    if extra_pos2>0:
        position2=int(a[(len(a)-2):(len(a)-1)])+int(b[(len(b)-2):(len(b)-1)])+extra_pos2
    else:
        position2=int(a[(len(a)-2):(len(a)-1)])+int(b[(len(b)-2):(len(b)-1)])
    extra_pos1=0
    if position2>5:
        extra_pos1=position2//6
        position2=position2%6
    if extra_pos1>0:
        position1=int(a[(len(a)-3):(len(a)-2)])+int(b[(len(b)-3):(len(b)-2)])+extra_pos1
    else:
        position1=int(a[(len(a)-3):(len(a)-2)])+int(b[(len(b)-3):(len(b)-2)])
    answer=str(position1)+str(position2)+str(position3)
    return answer
    
def ndom_multiply (a,b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    c=a*b
    answer=decimal_to_ndom(c)
    return answer