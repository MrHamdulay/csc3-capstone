import math
def ndom_to_decimal (a):
    ans=0
    strNum=str(a)
    if len(strNum)==1:
        dig1=strNum[0:1]
        ans+=int(dig1)
    elif len(strNum)==2:
        dig1=strNum[0:1]
        dig2=strNum[1:2]
        ans+=int(dig1)*6+int(dig2)
    elif len(strNum)==3:
        dig1=strNum[0:1]
        dig2=strNum[1:2]
        dig3=strNum[2:3]   
        ans+=int(dig1)*36+int(dig2)*6+int(dig3)
    return ans     

def decimal_to_ndom (a):
    ans=0
    if a%36==0: ans=100*(a//36)
    elif a//36==0:
        ans=int(str(a//6)+str(a%6))
    elif a>36:
        num36=100*(a//36)
        num6=0
        digits=0
        test6=a - 36*(a//36)
        if test6<6:
            digits=test6
            num6=0
        elif test6>5:
            digits=test6%6
            num6=test6//6
        ans=num36+int(str(num6)+str(digits))
        
    return int(ans)
    
def   ndom_add (a, b):
    numA=ndom_to_decimal (a)
    numB=ndom_to_decimal (b)
    sumAB=decimal_to_ndom(numA+numB)
    return sumAB
def ndom_multiply (a, b):
    numA=ndom_to_decimal (a)
    numB=ndom_to_decimal (b)
    mulAB=decimal_to_ndom(numA*numB)
    return mulAB