Cost=eval(input("Enter the cost (in cents):\n"))
Sum=0
while(Sum<Cost and Cost>0):
    e=eval(input("Deposit a coin or note (in cents):\n"))
    Sum=Sum+e
Change=Sum-Cost
p100=100
p25=25
p10=10
p5=5
p1=1

t100=Change//p100 #t100 means number of $1 notes 
Change=Change-t100*100
t25=Change//p25
Change=Change-t25*25
t10=Change//p10
Change=Change-t10*10
t5=Change//p5
Change=Change-t5*5
t1=Change//p1
Change=Change-t1*1
if(Cost>0 and (t100>0 or t25>0 or t10>0 or t5>0 or t1>0)):
    print("Your change is:")
if(t100>0):
    print(t100," x $1",sep="")
if(t25>0):
    print(t25," x 25c",sep="")
if(t10>0):
    print(t10," x 10c",sep="")
if(t5>0):
    print(t5," x 5c",sep="")
if(t1>0):
    print(t1," x 1c",sep="")