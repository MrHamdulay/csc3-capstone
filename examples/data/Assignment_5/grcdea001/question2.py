"""Program to calcuate the change needed for a given price and coins given Prac 5 Question 2
Dean Gracey
4/15/2014"""


cost = eval(input("Enter the cost (in cents):\n"))
given = 0
one=0
five= 0
ten = 0
tfive = 0
dollar = 0
change_needed= False
while (given<cost):
    given = given + eval(input("Deposit a coin or note (in cents):\n"))
change = given - cost   


#minuses largest ammount possible from change
while(change>=100):
    dollar+=1
    change-=100
    change_needed = True
    
while(change>=25):
    tfive+=1
    change-=25 
    change_needed = True

while(change>=10):
    ten+=1
    change-=10
    change_needed = True
    
while(change>=5):
    five+=1
    change-=5
    change_needed = True
    
while(change>=1):
    one+=1
    change-=1
    change_needed = True


if (change_needed): # to ensure only prints if there ischange   
    print("Your change is:")
    if(dollar!=0):
        print(dollar , "x" , "$1", sep = " ")
    if(tfive!=0):
        print(tfive , "x" , "25c", sep = " ")
    if(ten!=0):
        print(ten , "x" , "10c", sep = " ")
    if(five!=0):
        print(five , "x" , "5c", sep = " ")
    if(one!=0):
        print(one , "x" , "1c", sep = " ")

