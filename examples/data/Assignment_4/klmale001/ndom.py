#ndom
#Kavir Ranchod   -   RNCKAV001
#01/04/2014

def ndom_to_decimal (a):
    """convert a number in base 6 to base 10"""
    a=str(a)
    dec=0
    if len(a)==4:
        #first digit:
        first=a[0]
        first=eval(first)
        dec+=(first*216)
        #second digit:
        second=a[1]
        second=eval(second)
        dec+=second*36
        #third digit
        third=a[2]
        third=eval(third)
        dec+=third*6
        #fourth digit
        fourth=a[3]
        fourth=eval(fourth)
        dec+=fourth
        return dec
    elif len(a)==3:
        #first digit
        first=a[0]
        first=eval(first)
        dec+=first*36
        #second digit
        second=a[1]
        second=eval(second)
        dec+=second*6
        #third digit
        third=a[2]
        third=eval(third)
        dec+=third
        return dec
    elif len(a)==2:
        #first digit
        first=a[0]
        first=eval(first)
        dec+=first*6
        #second digit
        second=a[1]
        second=eval(second)
        dec+=second
        return dec
    elif len(a)==1:
        #only digit
        return a
    
def decimal_to_ndom (a):
    rem1=a%6
    y=a//6
    rem2=y%6
    b=y//6
    rem3=b%6
    c=b//6
    if rem3==0:
        ans=(str(rem2)+str(rem3))
        ans=eval(ans)
    elif rem2==0 and rem3==0:
        ans=(str(rem1))
        ans=eval(ans)
    else:
        ans=(str(rem3)+str(rem2)+str(rem1))
        ans=eval(ans)
    return ans

def ndom_add (a,b):
    """convert 2 numbers into decimal, add them, and convert back to ndom, 
    therefore adding numbers in ndom(base 6)"""
    return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))

def ndom_multiply (a,b):
    return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))