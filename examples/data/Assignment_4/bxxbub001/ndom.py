"""creates Ndom Numbers"""

def ndom_to_decimal(n):
    
    ndom = ""
    digit1=""
    digit2=""
    digit3=""
    findUnit=""
    strDig1=""
    strDig2=""
    strDig3=""
    if n > 5:
        if len(str(n)) ==1:
            ndom = n+4
            return ndom
        
        elif len(str(n))==2 and n<36:
            digit1 = n//6
            digit2=n-(digit1*6)#to find the unit
            strDig1=str(digit1)
            strDig2=str(digit2)
            ndom=eval(strDig1+strDig2)
            return ndom
        elif n>35:
            digit1 = n//36
            digit2=(n//6)-6#to find the 10
            digit3=n%6
            strDig1=str(digit1)
            strDig2=str(digit2)
            strDig3=str(digit3)
            ndom=eval(strDig1+strDig2+strDig3)
            return ndom            
        
        
    else:
        ndom = n
        return ndom

            
            
            
            
            
#ndom_to_decimal()
            
        