"""Priyanka Goberdhan
15/04/14
question three: change calculator"""

x=eval(input("Enter the cost (in cents):\n"))
y=0

while (x>y):
    y1=eval(input("Deposit a coin or note (in cents):\n"))
    y=y+y1

z=y-x
if (z>0):
    print("Your change is:")
    if((z//100)>0):
        print((z//100),"x $1")
        z=z-(100*(z//100))

    if((z//25)>0):
        print((z//25),"x 25c")
        z=z-(25*(z//25))
            
    if((z//10)>0):
        print((z//10),"x 10c")
        z=z-(10*(z//10))
                
    if((z//5)>0):
        print((z//5),"x 5c")
        z=z-(5*(z//5))
                    
    if((z//1)>0):
        print((z//1),"x 1c")
        z=z-(1*(z//1))