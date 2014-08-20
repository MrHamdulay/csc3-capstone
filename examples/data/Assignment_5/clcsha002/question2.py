"""question 2 assignment 5
Shannon clacey
15 april 2014"""

#naming variables and using sum as a sentinel

x = eval (input("Enter the cost (in cents): \n")) #assignment of random variable to get input of amount owing from user
sum = 0
while sum< x: #checking to see that the amount paid is more than the amount needed
    z = eval (input("Deposit a coin or note (in cents): \n")) #assignment of a random variable to get an input of amount paid from the user
    sum += z

#naming all the variables used to calculate the change where the difference calculates the amount remaining each time and the change is the number per unit i.e. 1$, 25c etc.
difference1 = sum - x
dollar_change = difference1//100
difference2 = (difference1-(dollar_change*100))
change_25= difference2//25
difference3 = (difference2-(change_25*25))
change_10=difference3//10
difference4 = (difference3-(change_10*10))
change_5=difference4//5
difference5= (difference4-(change_5*5))
change_1=difference5//1

#now creating a loop to print the amount of change provided that the amount given is not equal to the amount needed
if difference1 != 0:
    print("Your change is:")
    if dollar_change > 0:
        print(dollar_change, "x $1")
    if change_25 >0:
        print(change_25, "x 25c")  
    if change_10 > 0:
        print(change_10, "x 10c")
    if change_5 >0:
        print(change_5, "x 5c")
    if change_1 >0:
        print(change_1, "x 1c")

