#ndom
#Sofia Palmer
#1 April 2014

def ndom_to_decimal(a):
    mod = 10
    rem = 0
    decimal = 0
    base = 1
    while (a >= 1):
        rem = a % mod
        a = (a - rem)/10
        decimal += rem * base
        base = base * 6
   
    return decimal
ndom_to_decimal('a')

def decimal_to_ndom(a): 
    divisor = 1
    place = 1
    while(divisor <= a):
        divisor *= 6
        place += 1    
    divisor /= 6
    place -= 1
    ans = 0
    while (place >= 1):
        ans += (a // divisor) * (10**(place-1))
        a -= divisor * (a//divisor)
        divisor = divisor / 6
        place = place - 1
   
    return ans
decimal_to_ndom('a')

def ndom_add(a,b):
    place = 0
    mod = 10
    ans = 0
    
    while ((10 ** place) <= a and (10 ** place) <= b):
      
        num_1 = a % mod
        num_2 = b % mod
        ans += (num_1 + num_2)
        mod *= 10     
        if (ans >= (6 * (10 ** place))):
            ans-= 6 * (10** place)
            a += (10**(place+1))     
        a -= num_1
        b -= num_2
        place += 1
ndom_addition ('a','b')  

def ndom_multiply(a,b):    
    dec_a = ndom_to_decimal(a)
    dec_b = ndom_to_decimal(b)
    f = dec_a * dec_b
    return decimal_to_ndom(f)
ndom_multiply('a','b')


    
    
    

        

    
    
    