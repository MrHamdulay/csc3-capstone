#Assigment 4 Q2
#B.Player
#30/03/2014

def decimal_to_ndom(a):
    num1=(a//36)
    num2=(a%36)
    num3=num2//6
    num4=num2%6
    dec= (num1*100)+(num3*10)+num4
    return(dec)
   

def ndom_to_decimal(a):
    num1=(a//100)
    num2=(a%100)
    num3=num2//10
    num4=num2%10
    ndom= (num1*36)+(num3*6)+num4
    return(ndom)    
   

def ndom_add(a,b): 
    ans = ndom_to_decimal(a)+ndom_to_decimal(b)
    return decimal_to_ndom(ans)

def ndom_multiply(a,b):
    ans = ndom_to_decimal(a)*ndom_to_decimal(b)
    return  decimal_to_ndom(ans)    

if __name__=='__main__':
    choice = input ("Choose test:\n")
    action = choice[:1]
    print ("calling function")
    if action == 'n' or action == 'd':
        num = int(choice[2:])
        if action == 'n':
            answer = ndom_to_decimal (num)
        else:
            answer = decimal_to_ndom(num)
    elif action == 'a' or action == 'm':
        num1, num2 = map (int, choice[2:].split(" "))
        if action == 'a':
            answer = ndom_add (num1, num2)
        else:
            answer = ndom_multiply (num1, num2)
    print ("called function")
    print (answer)
    