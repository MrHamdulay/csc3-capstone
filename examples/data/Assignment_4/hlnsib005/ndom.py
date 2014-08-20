import ndom
def ndom_to_decimal(a):
    a= str(a)
    string1= a[0]  #1524
    string2= a[1:1]
    string3= a[2:2]
    string4= a[3:3]
    answer=int(a[0])
    for j in range(0+(len(a)-1)):
        answer=answer*6  #1*6    answer=1*6
        answer= answer+int(a[j+1])     #answer= 6+5
    return answer               #6+5
        
    
                                               #1 
                                               #     X6
                                               #5    add 5
                                               #11
                                               #     X6
                                               #66   add 2
                                               #68
                                               #     X6
                                               #408  add 4
                                             #412 new number        
def decimal_to_ndom(a):
    number=a
    temp=""
    product=1
    while product>0 :
        product= number//6                 #68= 412//6
        remainder= number-6*(product)      #4=  number-6(product)
        temp=temp+ str(remainder)              #temp=4
        number=product                  #a//number = 68
    return (temp[::-1])    
    
def ndom_add(a,b):
    first= ndom.ndom_to_decimal(a)
    second=ndom.ndom_to_decimal(b)
    answer=first+second
    return ndom.decimal_to_ndom(answer)
    
def ndom_multiply(a,b):
    first= ndom.ndom_to_decimal(a)
    second=ndom.ndom_to_decimal(b)
    answer=first*second
    return ndom.decimal_to_ndom(answer)    
    