def decimal_to_ndom(a):
    
    hundreds=0
    tens=0
    units=0
    remainder=0
    
    if a>36:
        if a%36==0:
            hundreds=a//36 
        
    
    elif a>5:
        if a%36==0: #if remainder of number when divided by 36 is 0 then the hundreds digit is the number divided by 36. eg 36//36=1
            hundreds=""
            tens=a//36
    
        else:
            hundreds="" #blank out the zero in the hundreds column.
            remainder=a//6 #eg 8//6=1
            tens=remainder #tens unit becomes 1
            units=a%6
   
    if a<=5:
        hundreds=""
        tens=""
        units=a  

    return(str(hundreds)+str(tens)+str(units))  



    