cost = int(input("Enter the cost (in cents):\n"))
pay = 0
while (pay < cost):
    pay += int(input("Deposit a coin or note (in cents):\n"))
excess = pay - cost
if (excess != 0): print ("Your change is: ")
number = 0
while ((number+1)*100 <= excess):
    number += 1
if (number != 0):
    print (number, "x $1")
excess += -number*100
number = 0
while ((number+1)*25 <= excess):
    number += 1
if (number != 0):
    print (number, "x 25c")
excess += -number*25
number = 0
while ((number+1)*10 <= excess):
    number += 1
if (number != 0):
    print (number, "x 10c")
excess += -number*10
number = 0
while ((number+1)*5 <= excess):
    number += 1
if (number != 0):
    print (number, "x 5c")
excess += -number*5
number = 0
while ((number+1)*1 <= excess):
    number += 1
if (number != 0):
    print (number, "x 1c")        