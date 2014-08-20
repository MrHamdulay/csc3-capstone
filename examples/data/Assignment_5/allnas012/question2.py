"""def main():
    cost=eval(input("Enter the cost (in cents):\n"))
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    x=0
    
    if (cost<5 and cost>=deposit):
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        change_due=deposit-change_owed
        #print("Your change is:\n")
        for i in range(change_due):
            x+=1
            one=change_due//1
            new_one=change_due-(one*1)
            print("Your change is:")
            if one !=0:
                print(one,"x 1c")                  
            break   
   
   
    elif (cost<10 and cost>=deposit):
        x+=5
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
         
        change_due=deposit-change_owed
        for i in range(chaneg_due):
            five=change_due//5
            new_five=change_due-(five*5)
            one=new_five//1
            new_one=new_five-(one*1)
            print("Your change is:")
            if five !=0:
                print(five,"x 5c")
            if one !=0:
                print(one,"x 1c")                          
            break      
   
    elif (cost<25 and cost>=deposit):
        x+=10
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
          
        change_due=deposit-change_owed
        for i in range(change_due):
            ten=change_due//10
            new_ten=change_due-(ten*10)
            five=new_ten//5
            new_five=new_ten-(five*5)
            one=new_five//1
            new_one=new_five-(one*1)
            print("Your change is:")
            if ten !=0:
                print(ten,"x 10c")
            if five !=0:
                print(five,"x 5c")                        
            if one !=0:
                print(one,"x 1c")                      
            break        
   
    elif (cost<100 and cost>=deposit):
        x=x+25
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
          
        change_due=deposit-change_owed
        for i in range(change_due):
            q=change_due//25
            new_q=change_due-(q*25)
            ten=new_q//10
            new_ten=new_q-(ten*10)
            five=new_ten//5
            new_five=new_ten-(five*5)
            one=new_five//1
            new_one=new_five-(one*1)
            print("Your change is:")
            if q !=0:
                print(q,"x 25c")     
            if ten !=0:
                print(ten,"x 10c")                    
            if five !=0:
                print(five,"x 5c")                    
            if one !=0:
                print(one,"x 1c")                  
            break
   
    elif (cost<=500 and cost>deposit):
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
          
        x=x+100
        change_due=deposit-change_owed
        for i in range(change_due):
            q=change_due//25
            new_q=change_due-(q*25)
            ten=new_q//10
            new_ten=new_q-(ten*10)
            five=new_ten//5
            new_five=new_ten-(five*5)
            one=new_five//1
            new_one=new_five-(one*1)
            print("Your change is:")
            if q !=0:
                print(q,"x 25c")
            if ten !=0:
                print(ten,"x 10c")        
            if five !=0:
                print(five,"x 5c")            
            if one !=0:
                print(one,"x 1c")
            break             
   
    elif ((cost<(cost+500)) and cost>=deposit):
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
          
        x=x+500
        change_due=deposit-change_owed
        for i in range(change_due):
            d=change_due//100
            new_d=change_due-(d* 100)
            q=new_d//25
            new_q=new_d-(q*25)
            ten=new_q//10
            new_ten=new_q-(ten*10)
            five=new_ten//5
            new_five=new_ten-(five*5)
            one=new_five//1
            new_one=new_five-(one*1)
            print("Your change is:")
            if d !=0:
                print(d,"x $1")
            if q !=0:
                print(q,"x 25c")
            if ten !=0:
                print(ten,"x 10c")        
            if five !=0:
                print(five,"x 5c")            
            if one !=0:
                print(one,"x 1c")
            break
         
                     
    
        
main()""" 


cost = eval(input("Enter the cost (in cents):\n"))
x = 0
while x < cost:
    x += eval(input("Deposit a coin or note (in cents):\n"))
if x > cost:
    difference = x - cost
    if difference != 0:
        print("Your change is:")
    dollar = difference//100
    if dollar != 0:
        print(dollar,'x $1')
    q = (difference- dollar*100)//25
    if q != 0:
        print(q,'x 25c')
    ten = (difference- dollar*100 - q*25)//10
    if ten != 0:
        print(ten,'x 10c')
    five= (difference- dollar*100 - q*25 - ten*10)//5
    if five != 0:
        print(five,'x 5c')
    one = (difference - dollar*100 - q*25 - ten*10 - five*5)//1
    if one != 0:
        print(one,'x 1c')
            
            