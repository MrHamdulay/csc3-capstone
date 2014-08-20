#Ndom
def ndom_to_decimal(num):
    
    if(num>99):
        digit = str(num)
        front = int(digit[0])*36
        middle = int(digit[1])*6
        back = int(digit[2])
        output = front+middle+back
    elif(num<=9):
        output= num
         
    else:   
        digit = str(num)
        front = int(digit[0])
        back =int(digit[1])
        output='' 
        if front==1:
            output= ((back))*10
        else:
            output=front*6+back
    return output
    
def decimal_to_ndom(a):
    output=''
    if(a>99):
        digit = str(a)
        front = (a)//36
        middle = (a-front*36)//6
        back = (a-front*36)-(middle*6)
        output =str(front)+str(middle)+str(back)
    elif( a <=5):
        output = a
    else:
        digit = str(a)
        front = int(digit)//6
        back= int(a)-(front*6)
        output = str(front)+str(back)
    return output
    #that converts a decimal number to Ndom n
def ndom_add(a, b):
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    output = decimal_to_ndom(a+b)
    #that adds 2 Ndom numbers
    return output
def ndom_multiply(a, b): 
    a=ndom_to_decimal(a)
    b=ndom_to_decimal(b)
    two = a*b
    output = two#decimal_to_ndom((two))
    return output
    #that multiples 2 Ndom numbers
if __name__== '__main__':
    main()