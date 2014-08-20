#Cherise Dube
#04 April 2014 
"""Program to convert to Ndom and back"""


def ndom_to_decimal (a):
    string_a=str(a)
    if len(string_a)==1 and a<=5:
        return int(a)
    elif len(string_a)==2:
        tens=string_a[:1]
        digits=string_a[1:]
        return ((int(tens))*6)+(int(digits))
    elif len(string_a)==3:
        hundreds=string_a[:1]
        tens=string_a[1:2]
        digits=string_a[2:]
        return ((int(hundreds))*36)+((int(tens))*6)+(int(digits))
    
def decimal_to_ndom (a):
    string_a=str(a)
    if len(string_a)==1:
        return a
    
    elif len(string_a)==2:
        digits=a%6
        tens=a//6
        return str(tens)+str(digits)
       
    elif len(string_a)==3:
        digits=a%6
        tens=(a//6)%6
        hundreds=(a//36)%6
        thousands=((a//36)//6)%6
        
        return str(thousands)+str(hundreds)+str(tens)+str(digits)
    
def ndom_add(a,b):
    string_a=str(a)
    string_b=str(b)
    
    a_digits=int(string_a[-1])
    b_digits=int(string_b[-1])
    digits_result=a_digits+b_digits
    if digits_result<=5:
        return digits_result
    else:
        return digits_result+4
    
    a_tens=int(string_a[-2])
    b_tens=int(string_b[-2])
    tens_result=a_tens+b_tens
    if tens_result<=5:
        return tens_result*6
    else:
        return (tens_result+4)*6
    
    
    a_hundreds=int(string_a[-3])
    b_hundreds=int(string_a[-3])
    hundreds_result=a_hundreds+b_hundreds
    if hundreds_result<=5:
        return hundreds_result*36
    else:
        return (hunreds_result+4)*36
    
    base_10_result=digits_result+tens_result+hundreds_result
    
    digits=base_10_result%6
    tens=(base_10_result//6)%6
    hundreds=(base_10_result//36)%6
    
    return str(hundreds)+str(tens)+str(digits)
    