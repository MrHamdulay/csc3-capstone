"""NDOM.py module for Question2
Tinotenda Chemvura (CHMTIN004)
31 March 2014"""

def ndom_to_decimal (a):
    stringa=str(a)

    if 100<=a<1000:                         #for 3 digit numbers
        first=eval(stringa[0:1:1])
        second=eval(stringa[1:2:1])
        third=eval(stringa[2:3:1])
        ndom=(first*36)+(second*6)+(third*1)

    elif 10<=a<100:                         #for 2 digit numbers
        first=eval(stringa[0:1:1])
        second=eval(stringa[1:2:1])
        ndom=(first*6)+(second*1)

    elif a<10:                              #for 1 digit numbers
        first=eval(stringa[0:1:1])
        ndom=(first*1)

    return ndom                            #return the value of ndom
#print(ndom_to_decimal(89))                  #testing if function works

def decimal_to_ndom (a):

    if 100 <= a < 1000:
        th = a//216

        if th<1:
            th=""
        r1 = a%216
        hund = r1//36
        r2 = r1%36
        tens = r2//6
        r3 = r2%6
        units = r3

        th, h, t, u = str(th), str(hund), str(tens), str(units)
        ndom = (th + h + t + u)

    elif 10 <= a < 100:
        hund = a//36

        if hund<1:
            hund=""
        r1 = a%36
        tens = r1//6
        r2 = r1%6
        units = r2

        h, t, u =str(hund), str(tens), str(units)
        ndom= (h + t + u)
        
    elif a<10:
        tens = a//6

        if tens<1:
            tens=""
        r1 = a%6
        units = r1

        t, u = str(tens), str(units)
        ndom = (t + u)
        
    ndom = eval(ndom)

    return ndom          

def ndom_add (a, b):

    ad = ndom_to_decimal(a)
    bd = ndom_to_decimal(b)
    dec_ans = ad + bd
    ndom_ans = decimal_to_ndom(dec_ans)

    return ndom_ans

def ndom_multiply (a, b):

    ad = ndom_to_decimal(a)
    bd = ndom_to_decimal(b)
    dec_ans = ad * bd
    ndom_ans = decimal_to_ndom(dec_ans)

    return ndom_ans
#_________________________Module ends here_____________________