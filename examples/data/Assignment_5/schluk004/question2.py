#Calculate change in given coins
#Luke Schwartzkopff
#13 April 2014

payt=0
change=0
cost=eval(input("Enter the cost (in cents):\n"))

while payt<cost:
    payt+=eval(input("Deposit a coin or note (in cents):\n"))

owed=payt-cost
num100=owed//100
num25=(owed-num100*100)//25
num10=(owed-num100*100-num25*25)//10
num5=(owed-num100*100-num25*25-num10*10)//5
num1=(owed-num100*100-num25*25-num10*10-num5*5)

numlist=[num100,num25,num10,num5,num1]
currlist=["$1","25c","10c","5c","1c"]

if owed>0:
 print("Your change is:")
 for i in range(len(numlist)):
     if numlist[i]>0:
         print(numlist[i],"x",currlist[i])


    
    
    
    


