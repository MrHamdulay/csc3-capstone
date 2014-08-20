#BLLKAT005
#Kate Bell
# 2 April 2014

def ndom_to_decimal (a):
    """converts a Ndom number to decimal"""
    decimal= eval(str(a)[0])
    for i in range(1,len(str(a))):
        decimal = decimal*6 + eval(str(a)[i])
    return decimal    #decimal is type int
             
def decimal_to_ndom (a):
    """converts a decimal number to Ndom"""
    ndom=0
    base = 1
    remain=-1
    quotient=a*6
    count=1
    while remain!=0:
        quotient=quotient//6
        remain= quotient%6 
        ndom=ndom+remain*base
        base=base*10
        if count==1:
            remain=-1
        count=count+1
    return ndom      #ndom is type int
    
def ndom_add (num1, num2):
    """adds 2 Ndom numbers"""
    #store numbers into lists
    a_list=[]
    b_list=[]
    for a in range (len(str(num1))):
        a_list = a_list+[eval(str(num1)[a])]
    for b in range (len(str(num2))):
        b_list = b_list+[eval(str(num2)[b])]
    
    carry = 0
    ndom = []
# a is bigger so loop through b
    if len(a_list)>=len(b_list):
        for i in range(-1,-len(b_list)-1,-1):
            remainder= (carry + a_list[i] + b_list[i])%6
            if remainder>0:
                ndom=ndom+[remainder]
            elif remainder == 0:
                ndom=ndom+[remainder]
                carry = (a_list[i] + b_list[i])//6
        first = []
        for j in range (len(a_list)-len(b_list)):
            first= first+[a_list[j]]
        first_reversed = first[::-1]
        ndom=ndom+first_reversed
        final_ndom=ndom[::-1]
        s=""
        for z in range (len(final_ndom)):
            s=s+str(final_ndom[z])
        ndom=eval(s)
        return ndom
        
# b is bigger so loop through a
    elif len(a_list)<len(b_list):
        for i in range(-1,-len(a_list)-1,-1):
            remainder= (carry + a_list[i] + b_list[i])%6
            if remainder>0:
                ndom=ndom+[remainder]
            elif remainder == 0:
                ndom=ndom+[remainder]
                carry = (a_list[i] + b_list[i])//6
            first=[]
            for j in range (len(b_list)-len(a_list)):
                first= first+[b_list[j]]
            
            first_reversed = first[::-1]
            ndom=ndom+first_reversed
            final_ndom=ndom[::-1]
            s=""
            for z in range (len(final_ndom)):
                s=s+str(final_ndom[z])
            ndom=eval(s)
            return ndom        

def ndom_multiply (a, b):
    """multiples 2 Ndom numbers"""
    a=ndom_to_decimal (a)
    b=ndom_to_decimal (b)    
    product = a*b
    prod_ndom = decimal_to_ndom (product) 
    return prod_ndom

def test(num):
    print(len(str(num)))