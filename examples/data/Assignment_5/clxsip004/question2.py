#Siphesihle Shaun Cele
#17 april 2014
#writing a program to simulate a vending machine.
import math

deposit=0  #initializing the bag value to zero.
#user input to calculate the cost of the good.
cost=eval(input("Enter the cost (in cents):\n"))

while deposit<cost:
    deposit+=eval(input("Deposit a coin or note (in cents):\n"))
    
if deposit>cost:
    Total= deposit-cost
    if Total!=0:
        print("Your change is:")
    
    money=Total//100     #statements that calculate the change in the different 5 ranges.
    cents=(Total-money*100)//25
    cents_2=(Total-money*100-cents*25)//10
    cents_3=(Total-money*100-cents*25-cents_2*10)//5
    cents_4=(Total-money*100-cents*25-cents_2*10-cents_3*5)//1
    
    if money!=0:  #if statements that will control what is displayed on the screen once the calculations are done.
        print(money,"x $1")
   
    if cents!=0:
        print(cents,"x 25c")
     
    if cents_2 !=0:
        print(cents_2,"x 10c")
   
    if cents_3 !=0:
        print(cents_3," x 5c")
      
    if cents_4 !=0:
        print(cents_4,"x 1c")
        
        
    

