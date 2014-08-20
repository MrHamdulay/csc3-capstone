def ndom_to_decimal (num):
        a=str(num)
        m=len(a)
        sum2=0
        for i in range(m):
                num1=int(a[i])
                newnum1=num1*(6**(m-1))
                m-=1
                sum2+=newnum1
        return sum2

def decimal_to_ndom (num):
        a=str(num)
        m=len(a)
        sum1=0   
        for i in range(m+1):
                num2=num%6
                newnum2=num2*(10**i)
                sum1+=newnum2
                num=num//6
        return (sum1)

def ndom_add (num1, num2):
        num1=ndom_to_decimal (num1)
        num2=ndom_to_decimal (num2)
        num3=num1+num2
        num3=decimal_to_ndom (num3)
        return num3

def ndom_multiply (num1, num2):
        num1=ndom_to_decimal (num1)
        num2=ndom_to_decimal (num2)
        num3=num1*num2
        num3=decimal_to_ndom (num3)
        return num3
                
        
         
    