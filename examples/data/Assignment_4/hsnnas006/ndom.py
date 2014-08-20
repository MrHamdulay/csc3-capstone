'''module for simple ndaom arithmetic
nasreen hoosain
21/04/14'''

#function to convert ndom to decimal
def ndom_to_decimal(ndom):
    ndom = str(ndom) #converts to string
    #ensure length of number is 3
    if len(ndom) == 1:
        ndom_len3 = '00'+ndom
    elif len(ndom) == 2:
        ndom_len3 = '0'+ndom
    else:
        ndom_len3 = ndom
    #decimal calculation; 1st digitx36, 2nd digitx6, 3rd digitx1
    dec = int(ndom_len3[0])*36 + int(ndom_len3[1])*6 + int(ndom_len3[2])
    return dec
    
#function to convert decimal to ndom
def decimal_to_ndom(dec):
    if 36 <= dec:
        ndom_1 = dec//36 #ndom digit 1
        dec = dec-(ndom_1*36)
        ndom_2 = dec//6 #ndom digit 2
        ndom_3 = dec-(ndom_2*6) #ndom digit 3
        ndom = str(ndom_1)+str(ndom_2)+str(ndom_3) #puts three digits together
    elif 6 <= dec:
        # no digit 1, since dec < 36
        ndom_2 = dec//6
        ndom_3 = dec-(ndom_2*6)  
        ndom = str(ndom_2)+str(ndom_3)
    else:
        ndom_3 = dec
        ndom = ndom_3
    ndom = eval(ndom)
    return ndom

#function to add 2 ndom numbers         
def ndom_add(a,b):
    dec_a = ndom_to_decimal(a)
    dec_b = ndom_to_decimal(b)
    ans = dec_a + dec_b
    ndom_ans = decimal_to_ndom(ans)
    return ndom_ans

#function to multiply 2 ndom numbers
def ndom_multiply(a,b):
    dec_a = ndom_to_decimal(a)
    dec_b = ndom_to_decimal(b)
    ans = dec_a * dec_b
    ndom_ans = decimal_to_ndom(ans)
    return ndom_ans   