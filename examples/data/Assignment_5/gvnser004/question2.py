cost=eval(input("Enter the cost (in cents):\n"))
sum1=0
"""countS1=0
count25c=0
count10c=0
count5c=0
count1c=0"""
count=[0,0,0,0,0]
values=["$1","25c","10c","5c","1c"]


while sum1<cost:
    c=eval(input("Deposit a coin or note (in cents):\n"))
    sum1+=c

change=sum1-cost

if(change>0):
    print("Your change is:")


while change>=100:
    count[0]+=1
    change-=100
    
    
while change>=25:
    count[1]+=1
    change-=25
    
while change>=10:
    count[2]+=1
    change-=10
    
while change>=5:
    count[3]+=1
    change-=5
    
while change>=1:
    count[4]+=1
    change-=1


for i in range(5):
    
    if(count[i]>0):
        print(count[i],"x",values[i])
        
