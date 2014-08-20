# Assignment 5: Question 2
# nckemm001
# 16 April 2014

def main():
    cost= eval(input("Enter the cost (in cents):\n"))
    t="p"
    if cost >0:
        while t == "p" :
            deposit = eval(input("Deposit a coin or note (in cents):\n"))
            sumdeposit = cost - deposit
            if sumdeposit <= 0:
                t= "m"
                break
            else :
                t= "p"
                cost = cost-deposit
        sumdeposit = -sumdeposit
                
        if sumdeposit > 0:
            print("Your change is:")
            
            l = str(sumdeposit)
            rem = len(l)
            
            if rem == 4:
                dollar = eval(l[0:2]) 
                dollar = str(dollar)
                print(dollar,"x $1")
                cent2 = eval(l[2:4]) 
                f = "k"
                w = 0
                while f == "k":
                    if cent2 >=25:
                        cent2 = cent2 -25
                        w +=1
                        f = "k"
                    else :
                        f = "b"
                        break
                if w > 0:
                    print(w,"x 25c")
                tri = "k"
                op = 0
                while tri == "k":
                    if cent2 >=10:
                        cent2 = cent2 -10
                        op +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op > 0:
                    print(op,"x 10c")
                tri = "k"
                op2 = 0
                while tri == "k":
                    if cent2 >=5:
                        cent2 = cent2 -5
                        op2 +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op2 > 0:
                    print(op2,"x 5c")
                tri = "k"
                op3 = 0
                while tri == "k":
                    if cent2 >=1:
                        cent2 = cent2 -1
                        op3 +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op3 > 0:
                    print(op3,"x 1c")
                
            elif r == 3:
                dollar = eval(l[0]) 
                dollar = str(dollar)
                print(dollar,"x $1")
                cent2 = eval(l[1:3]) 
                f = "k"
                w = 0
                while f == "k":
                    if cent2 >=25:
                        cent2 = cent2 -25
                        w +=1
                        f = "k"
                    else :
                        f = "b"
                        break
                if w > 0:
                    print(w,"x 25c")
                tri = "k"
                op = 0
                while tri == "k":
                    if cent2 >=10:
                        cent2 = cent2 -10
                        op +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op > 0:
                    print(op,"x 10c")
                tri = "k"
                op2 = 0
                while tri == "k":
                    if cent2 >=5:
                        cent2 = cent2 -5
                        op2 +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op2 > 0:
                    print(op2,"x 5c")
                tri = "k"
                op3 = 0
                while tri == "k":
                    if cent2 >=1:
                        cent2 = cent2 -1
                        op3 +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op3 > 0:
                    print(op3,"x 1c")   
                
            elif r ==2:
                cent2 = eval(l[0:2]) 
                f = "k"
                w = 0
                while f == "k":
                    if cent2 >=25:
                        cent2 = cent2 -25
                        w +=1
                        f = "k"
                    else :
                        f = "b"
                        break
                if w > 0:
                    print(w,"x 25c")
                tri = "k"
                op = 0
                while tri == "k":
                    if cent2 >=10:
                        cent2 = cent2 -10
                        op +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op > 0:
                    print(op,"x 10c")
                tri = "k"
                op2 = 0
                while tri == "k":
                    if cent2 >=5:
                        cent2 = cent2 -5
                        op2 +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op2 > 0:
                    print(op2,"x 5c")
                tri = "k"
                op3 = 0
                while tri == "k":
                    if cent2 >=1:
                        cent2 = cent2 -1
                        op3 +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op3 > 0:
                    print(op3,"x 1c")          
                
            elif r==1:
                cent2 = eval(l[0:1]) 
                tri = "k"
                op2 = 0
                while tri == "k":
                    if cent2 >=5:
                        cent2 = cent2 -5
                        op2 +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op2 > 0:
                    print(op2,"x 5c")
                tri = "k"
                op3 = 0
                while tri == "k":
                    if cent2 >=1:
                        cent2 = cent2 -1
                        op3 +=1
                        tri = "k"
                    else :
                        tri = "b"
                        break
                if op3 > 0:
                    print(op3,"x 1c")
        
            
        
main()
    