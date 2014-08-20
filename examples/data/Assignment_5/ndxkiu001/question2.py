#Kiuran Naidoo
#Assignment 5
#Question 2

cents = eval(input("Enter the cost (in cents):\n")) 
change = 0
while cents > 0: #Check if money is still required
    cents = cents-eval(input("Deposit a coin or note (in cents):\n")) #update money still required
    if cents < 0:
        change = abs(cents) #Get change defecit 
ochange = change        #capture original change
d = change//100 #Store number of dollars
change = change - (d*100) #Change amount of change still needed
q = change//25 #Store number of quarters
change = change-(q*25) #Change amount of change still needed
di = change//10 #Store number of dimes
change = change-(di*10)#Change amount of change still needed
n = change//5 #Store number of nickels
change = change - (n*5) #Change amount of change still needed
p = change#Store number of dimes

#Print Change if any
if ochange > 0: 
    print( "Your change is:" )
    if d > 0:
        print( d, "x $1" )
    if q > 0:
        print( q, "x 25c" )
    if di > 0:
        print( di, "x 10c" )
    if n > 0:
        print( n, "x 5c" )
    if p > 0:
        print( p, "x 1c")
