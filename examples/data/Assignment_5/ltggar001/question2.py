'''program that calculates the required change once the price has been reache/exceded
Gareth Lategan
15-04-2014'''

TP = eval(input("Enter the cost (in cents):\n")) #TP = Total Price
AP = 0 #AP = Ammount Paid
while AP<TP: #Keeps asking for more money until it's over the threshold
    CP = eval(input("Deposit a coin or note (in cents):\n")) #CP = Current Payment
    AP = AP + CP
D = AP - TP #D = Difference
a = 0
b = 0
c = 0
d = 0
e = 0
if D!=0:
    print("Your change is:")
while D > 0:
    if D >= 100:
        a += 1
        D = D - 100
    elif D >= 25:
        b += 1
        D = D - 25
    elif D >= 10:
        c += 1
        D = D - 10
    elif D >= 5:
        d += 1
        D = D - 5
    elif D >= 1:
        e += 1
        D = D - 1
if a > 0:
    print(a,"x $1")
if b > 0:
    print(b,"x 25c")
if c > 0:
    print(c,"x 10c")
if d > 0:
    print(d,"x 5c")
if e > 0:
    print(e,"x 1c")