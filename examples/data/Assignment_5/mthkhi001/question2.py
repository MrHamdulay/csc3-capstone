#Khiraad Mathura
#MTHKHI001
#Assignment 5 question 2

cost = eval(input("Enter the cost (in cents):\n"))

payment = 0
while payment < cost:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    payment = payment + deposit
    
change = payment - cost
if(change == 0):
    print("")
    
else:
    print("Your change is:")
    
    dollar = change// 100
    dollarloss = change - (dollar * 100)
    if(dollar >= 1):
        print(str(dollar) + " " + "x $1")
    
    quarter = dollarloss// 25
    quarterloss = dollarloss - (quarter * 25)
    if(quarter >= 1):
        print(str(quarter) + " " + "x 25c")
    
    tencent = quarterloss// 10
    tencentloss = quarterloss - (tencent * 10)
    if(tencent >= 1):
        print(str(tencent) + " " + "x 10c")
    
    fivecent = tencentloss// 5
    fivecentloss = tencentloss - (fivecent * 5)
    if(fivecent >=1):
        print(str(fivecent) + " " + "x 5c")
    
    onecent = fivecentloss//1
    onecentloss = fivecentloss - (onecent * 1)
    if(onecent >= 1):
        print(str(onecent) + " " + "x 1c")

