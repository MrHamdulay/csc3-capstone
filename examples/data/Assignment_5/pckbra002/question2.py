"""Program to simulate a vending machine and calculate change based on amount paid"""
#Brandon Pickup
#2014/04/14
#Assignment 5 Question 2
cost = eval(input("Enter the cost (in cents):\n"))#get the cost of the item bought from the user
paid = 0
while paid<cost:#Continues to ask for a payment while the user has paid less than the cost of the item
    paid += eval(input("Deposit a coin or note (in cents):\n"))
change = paid-cost#determines the difference / what is owed back to the user
changePrint = "Your change is:\n"
dollar = change//100#number of dollars worth of change is simply the change amount integer divided by 100cents
change = change%100#remaining change is the remainder after the dollar calculation has been made
changeCheck = change#checks whether there is change or not
if dollar != 0:#only prints the number of dollars if there are actually dollars as a form of change
    changePrint += str(dollar)+" x "+chr(36)+"1\n"#builds the string that will be displayed to the user as change, chr(36) is simply the ASCII value for a dollar symbol
twentyFive = change//25
change = change%25
if twentyFive != 0:
    changePrint += str(twentyFive)+" x 25c\n"
ten = change//10
change = change%10
if ten != 0:
    changePrint += str(ten)+" x 10c\n"
five = change//5
change = change%5
if five != 0:
    changePrint += str(five)+" x 5c\n"
if change != 0:
    changePrint += str(change)+" x 1c\n"
if changeCheck:print(changePrint)#prints the string filled with the breakdown of change owed to the user, only if there is any change at all
    