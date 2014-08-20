#program simulating a vending machine to calculate change
#gary Finkelstein
#15 April 2014

#allow for user to enter cost

user_input = input("Enter the cost (in cents): \n")
cost = eval(user_input)

#method used to determine the total amount entered by the user 
def getTotal():
    totalinput = 0
    while totalinput< cost:
        x = eval (input("Deposit a coin or note (in cents): \n"))
        totalinput = totalinput + x
    return totalinput

deposited_amount = getTotal()

#method used to determine how much change must be presented
def determineChange(value):
    
    diff = value - cost
    b = diff//100
    c = (diff-(b*100))
    d= c//25
    e = (c-(d*25))
    f=e//10
    g = (e-(f*10))
    h=g//5
    i= (g-(h*5))
    j=i//1
    if diff != 0:
        print("Your change is:")
        if b > 0:
            print(b, "x $1")
        if d >0:
            print(d, "x 25c")  
        if f > 0:
            print(f, "x 10c")
        if h >0:
            print(h, "x 5c")
        if j >0:
            print(j, "x 1c")    

determineChange(deposited_amount)