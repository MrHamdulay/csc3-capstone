#A program to ask the user to put in the cost of something in cents and keep on asking for deposit until the Cost is met/exceeded...
#Jacob Ntesang
#13/04/2014
#stated on 02:00 to 02:30 am and modified again from 08:00 am till Breakfast

C=0
Cost=eval(input("Enter the cost (in cents):\n"))
if Cost < 0:
 Deposit=eval(input("Deposit a coin or note (in cents):\n"))
 C+=Deposit

#while the cost is less than the cost of an item,get as much deposit as infintely if possible till it is met or exceeded
while C < Cost:
    Deposit=eval(input("Deposit a coin or note (in cents):\n"))#Prompt the user to enter the Deposit till the cost is met or exceeded
    C+=Deposit
    #print(C)
M=C-Cost#Calculating the change
if M == 0:
    print("")
if M > 0:
    print("Your change is:\n",end="")
if M >= 100:
    x=M//100#Calculating that must be categorised in dollars
    x=str(x)+ " x $1"
    print(x)
    M=M%100#Calculate Change in cents(25)
    #print(M)
if M >= 25:
    y=M//25
    U=str(y)+ " x 25c"
    print(U)
    M=M-y*25#Calculate the change left after (25 cents change is calculated)
if M >= 10 and M < 25:
    z=M//10
    a=str(z)+ " x 10c"
    print(a)
    M=M-z*10
if M < 10 and M >= 5:
    five=M//5
    b=str(z)+ " x 5c"
    print(b)
    M=M-five*5
if M >= 1:
    d=M//1
    d=str(M)+ " x 1c"
    print(d)

    
