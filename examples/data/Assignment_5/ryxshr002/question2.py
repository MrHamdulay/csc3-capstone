"""Shriya Roy
16 April 2014
program to find change"""



def main():
    #getting input from user
    y=eval(input("Enter the cost (in cents):\n"))
    if y == 0:
        return
    x=eval(input("Deposit a coin or note (in cents):\n"))
    #while statement to meet the deposit
    while x<y:
        x +=eval(input("Deposit a coin or note (in cents):\n"))
        
        #while statement to get change 
    while x>=y:
        if x != y:
            print("Your change is:")
        else:
            break
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        if (x-y)>=100:
            a= (x-y) // 100
            print(a, "x", "$1")
        if (x-y) -(a*100) >= 25:
            b= ((x-y)-(a*100))//25
            print(b, "x", "25c")
        if (x-y)-(a*100)-(b*25) >=10:
            c= ((x-y)-(a*100)-(b*25))//10
            print(c, "x", "10c")
        if (x-y)-(a*100)-(b*25) - (c*10) >= 5:
            d=( (x-y)-(a*100)-(b*25)-(c*10))//5
            print(d, "x", "5c")    
        if(x-y)-(a*100)-(b*25)-(c*10)-(d*5)>= 1:
            e=((x-y)-(a*100)-(b*25)-(c*10))//1
            print(e, "x", "1c")
            
        
        break


    
         

main()
