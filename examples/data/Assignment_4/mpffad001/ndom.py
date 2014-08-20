"""A program to change ndom numbers to decimals and add them and multiply
By Fadzai Mupfunya
01 April 2014"""
import ndom
def ndom_to_decimal(a):
        b=str(a)
        l=len(b)
        if l==2:
                c=b[:1]
                d=b[1:2]
                base_ten=((eval(c)*6)+(eval(d)*1))
                return (base_ten)                
        
        if l==3:
                c=b[:1]
                d=b[1:2]
                e=b[2:3]
                base_ten2=((eval(c)*36)+(eval(d)*6)+(eval(e)*1))
                return(base_ten2)

def decimal_to_ndom(a):
        b=str(a)
        p=(a//6)
        r=(a%6)
        s=(p//6)
        t=(p%6)
        u=(s//6)
        v=(s%6)
        w=(u//6)
        q=(u%6)
        num=int(str(q)+str(v)+str(t)+str(r))
        return (num)
                
def ndom_add (n1, n2):
        n1=ndom_to_decimal(n1)
        n2=ndom_to_decimal(n2)
        add=n1+n2
        final=decimal_to_ndom(add)
        return final
def ndom_multiply (n1, n2):
        n1=ndom_to_decimal(n1)
        n2=ndom_to_decimal(n2)
        mult=n1*n2
        final=decimal_to_ndom(mult)
        return final        

                
                
                


        