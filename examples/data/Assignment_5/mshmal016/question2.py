cost=eval(input("Enter the cost (in cents):\n"))
dep=0
#check deposit relative to cost
while cost>dep:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    dep=dep+deposit
    if cost<=dep:continue
       
dif=dep-cost
dollar=dif//100
dif=dif-dollar*100
#print(dif)

quarter=dif//25
#print(quarter)
dif=dif-quarter*25

tens=dif//10
dif=dif-tens*10

fives=dif//5
dif=dif-fives*5

ones=dif//1 
dif=dif-ones

if dif==0:
    print("Your change is:")
    if dollar>0:
        print(dollar,"x $1")
    if quarter>0:
        print(quarter,"x 25c")
    if tens>0:
        print(tens,"x 10c")
    if fives>0:
        print(fives,"*5c")
    if ones>0:
        print(ones,"*1c")
        
    
    



