"""Program to calculate change from a vending machine
Telisha Ramlall
12/04/2014"""

def main():
    
    cost= eval(input("Enter the cost (in cents):\n"))
    
    terminate="no"
    
    if cost >0:
        while terminate == "no":
            payment = eval(input("Deposit a coin or note (in cents):\n"))
            payment_sum = cost - payment
            if payment_sum <= 0:
                terminate= "m"
                break
            else :
                terminate= "no"
                cost = cost-payment
        payment_sum = -payment_sum
                
        if payment_sum > 0:
            print("Your change is:")
         
            l = str(payment_sum)
            r = len(l)

            if r == 4:
                dollar = eval(l[0:2]) 
                dollar = str(dollar)
                print(dollar,"x $1")
                cents = eval(l[2:4]) 
                terminate1 = "no"
                w = 0
                while terminate1 == "no":
                    if cents >=25:
                        cents = cents -25
                        w +=1
                        terminate1 = "no"
                    else :
                        terminate1 = "b"
                        break
                if w > 0:
                    print(w,"x 25c")
                terminate2= "no"
                op = 0
                while terminate2== "no":
                    if cents >=10:
                        cents = cents -10
                        op +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op > 0:
                    print(op,"x 10c")
                terminate2= "no"
                op2 = 0
                while terminate2== "no":
                    if cents >=5:
                        cents = cents -5
                        op2 +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op2 > 0:
                    print(op2,"x 5c")
                terminate2= "no"
                op3 = 0
                while terminate2== "no":
                    if cents >=1:
                        cents = cents -1
                        op3 +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op3 > 0:
                    print(op3,"x 1c")
                
            elif r == 3:
                dollar = eval(l[0]) 
                dollar = str(dollar)
                print(dollar,"x $1")
                cents = eval(l[1:3]) 
                terminate1 = "no"
                w = 0
                while terminate1 == "no":
                    if cents >=25:
                        cents = cents -25
                        w +=1
                        terminate1 = "no"
                    else :
                        terminate1 = "b"
                        break
                if w > 0:
                    print(w,"x 25c")
                terminate2= "no"
                op = 0
                while terminate2== "no":
                    if cents >=10:
                        cents = cents -10
                        op +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op > 0:
                    print(op,"x 10c")
                terminate2= "no"
                op2 = 0
                while terminate2== "no":
                    if cents >=5:
                        cents = cents -5
                        op2 +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op2 > 0:
                    print(op2,"x 5c")
                terminate2= "no"
                op3 = 0
                while terminate2== "no":
                    if cents >=1:
                        cents = cents -1
                        op3 +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op3 > 0:
                    print(op3,"x 1c")   
                
            elif r ==2:
                cents = eval(l[0:2]) 
                terminate1 = "no"
                w = 0
                while terminate1 == "no":
                    if cents >=25:
                        cents = cents -25
                        w +=1
                        terminate1 = "no"
                    else :
                        terminate1 = "b"
                        break
                if w > 0:
                    print(w,"x 25c")
                terminate2= "no"
                op = 0
                while terminate2== "no":
                    if cents >=10:
                        cents = cents -10
                        op +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op > 0:
                    print(op,"x 10c")
                terminate2= "no"
                op2 = 0
                while terminate2== "no":
                    if cents >=5:
                        cents = cents -5
                        op2 +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op2 > 0:
                    print(op2,"x 5c")
                terminate2= "no"
                op3 = 0
                while terminate2== "no":
                    if cents >=1:
                        cents = cents -1
                        op3 +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op3 > 0:
                    print(op3,"x 1c")          
                
            elif r==1:
                cents = eval(l[0:1]) 
                terminate2= "no"
                op2 = 0
                while terminate2== "no":
                    if cents >=5:
                        cents = cents -5
                        op2 +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op2 > 0:
                    print(op2,"x 5c")
                terminate2= "no"
                op3 = 0
                while terminate2== "no":
                    if cents >=1:
                        cents = cents -1
                        op3 +=1
                        terminate2= "no"
                    else :
                        terminate2= "b"
                        break
                if op3 > 0:
                    print(op3,"x 1c")
        
            
        
main()
    