"""question 2- assignment 5
prinesan govender
14 april 2014"""
cost= eval(input("Enter the cost (in cents):\n"))
sum=0

while(sum<cost):
    add= eval(input("Deposit a coin or note (in cents):\n"))
    sum=sum+add

excess=sum-cost
if(excess!=0):
    no100= excess//100
    rem1= excess%100
    no25= rem1//25
    rem2= rem1%25
    no10= rem2//10
    rem3= rem2%10
    no5= rem3//5
    rem4= rem3%5
    no1=rem4
    print("Your change is:")
    if(no100!=0): print(no100,"x $1")
    if(no25!=0): print(no25,"x 25c")
    if(no10!=0): print(no10,"x 10c")
    if(no5!=0): print(no5,"x 5c")
    if(no1!=0): print(no1,"x 1c")    





    
    
    
    
