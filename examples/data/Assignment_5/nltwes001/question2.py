#ASSIGNMENT 5
#NLTWES001
#QUESTION 2

cost=eval(input("Enter the cost (in cents):"'\n'))

#Payment
paid=0
while paid<cost:
    paid=paid+eval(input("Deposit a coin or note (in cents):"'\n'))

#Calculate and Display Change
surplus=paid-cost
if surplus!=0:
    print("Your change is:")
if surplus>=100:
    dollars=str(surplus//100)
    print(dollars," x ","$1",sep="")
    surplus=surplus-((eval(dollars))*100)
if surplus>=25:
    quarters=str(surplus//25)
    print(quarters," x ","25c",sep="")
    surplus=surplus-((eval(quarters))*25)
if surplus>=10:
    dimes=str(surplus//10)
    print(dimes," x ","10c",sep="")
    surplus=surplus-((eval(dimes))*10)
if surplus>=5:
    nickels=str(surplus//5)
    print(nickels," x ","5c",sep="")
    surplus=surplus-((eval(nickels))*5)
if surplus>=1:
    pennies=str(surplus//1)
    print(pennies," x ","1c",sep="")
    surplus=surplus-((eval(pennies))*1)




