cost=eval(input("Enter the cost (in cents):\n"))
money=0;

while(cost>money):
    money=money+eval(input("Deposit a coin or note (in cents):\n"))
change=money-cost

twentyfive=0
tencent=0
fivecent=0
onecent=0

dollar=change//100

twentyfive=change%100//25

tencent=change%100%25//10
    
fivecent=change%100%25%10//5

onecent=change%100%25%10%5//1

if change>0:
    print("Your change is:")

if(dollar>0):
    print(dollar,"x $1")
if(twentyfive>0):
    print(twentyfive,"x 25c")        
if(tencent>0):
    print(tencent,"x 10c")
if(fivecent>0):
    print(fivecent,"x 5c")        
if(onecent>0):
    print(onecent,"x 1c")        
        
    
