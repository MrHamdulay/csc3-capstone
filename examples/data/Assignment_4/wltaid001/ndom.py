#Aiden Walton
#WLTAID001
# Ndom module

def ndom_to_decimal (a):
        dec1=a//100
        dec2=(a//10)-(dec1*10)
        dec3=a%10
        answer=((dec1*36)+(dec2*6)+dec3)
        return answer
def decimal_to_ndom (a):
        a=int(a)
        dec3=a%6
        dec2=(a//6)%6
        dec1=(a//36)%6
        answer=((dec1*100)+(dec2*10)+dec3)               
        return int(answer)
def ndom_add (a, b):
        a=ndom_to_decimal(a)
        b=ndom_to_decimal(b)
        answer=a+b
        answer=decimal_to_ndom(answer)
        return answer
def ndom_multiply (a,b):
        a=ndom_to_decimal(a)
        b=ndom_to_decimal(b)
        answer=a*b
        answer=decimal_to_ndom(answer)
        return answer
