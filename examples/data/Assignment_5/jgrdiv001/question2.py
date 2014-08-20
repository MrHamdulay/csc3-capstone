"""PROGRAM TO CREATE A VEDING MACHINE THAT RETURNS YOUR CHANGE
DIVAN JAGERS
JGRDIV001
15 APRIL 2014"""

x=eval(input("Enter the cost (in cents):\n")) #THE USER ENTERS THE COST
y=0 # INITIAL VALUE OF COINS ENTERED
while y < x: #RUNS AS LONG AS COINS ENTERED IS LESS THAN THE COST
    z=eval(input("Deposit a coin or note (in cents):\n")) #THE USER ENTERS COINS
    y+=z
z=y-x                   #THE CHANGE IN CENts
#KEEPS ON DIVINDING THE CHANGE              
#THE REMAINDER OF THE CHange
#the double of the variable is the qoutient of the remainder divided by the relevant unit of money)
#the single of the variable represents the change left over
h=z//100                
t=z-(h*100)               
tt=t//25
ten=t-(tt*25)
tenten=ten//10
five=ten-(tenten*10)
fivefive=five//5
one=five-(fivefive*5)
oneone=one//1
if z > 0:
    print("Your change is:") #PRINTS THE QUOTIENT OF EACH STEP ABOVE AND THE UNIT OF money
if h > 0:
    print(h,"x $1")
if tt > 0:
    print(tt,"x 25c")
if tenten > 0:
    print(tenten,"x 10c")
if fivefive > 0:
    print(fivefive,"x 5c")
if oneone >0:
    print(oneone,"x 1c")

       