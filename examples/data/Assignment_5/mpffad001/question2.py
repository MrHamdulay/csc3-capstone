#a program to simulate a vending machine
#fadzai mupfunya
#13 April 2014


x=0
dep=0 #the deposits that the user enters
cost=eval(input("Enter the cost (in cents):" '\n')) #the cost needed for the item
while dep<cost:
    x=eval(input("Deposit a coin or note (in cents):" '\n')) #when the user has typed in a value less than the cost
    dep+=x
    if dep==cost: break
    elif dep>cost: break
    
change=dep-cost #to calculate the change
#to convert the change to dollars, 25c, 10c and 5c
div1=change//100 
rem1=change%100
div2=rem1//25
rem2=rem1%25
div3=rem2//10
rem3=rem2%10
div4=rem3//5
rem4=rem3%5
div5=rem4//1
rem5=rem4%1
if change!=0:
            print("Your change is:")
x=[div1, div2, div3, div4, div5]
if(x[0] !=0):
            print(div1, "x $1")       
if(x[1] !=0):
            print(div2, "x 25c")      
if(x[2] !=0):
            print(div3, "x 10c")         
if(x[3] !=0):
            print(div4, "x 5c")         
if(x[4] !=0):
            print(div5, "x 1c")         
    
      
             
            
        
       
    
    
    

    
