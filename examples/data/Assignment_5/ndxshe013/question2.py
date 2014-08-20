


x = eval(input("Enter the cost (in cents):\n"))
y = 0

while y < x:
    y = y + eval(input("Deposit a coin or note (in cents):\n"))




z = y - x
if z != 0:
    print("Your change is:" )

if z// 100 != 0:
    print(z//100,"x $1")
    
a = z - (z//100)*100 
if a //25 != 0:
    print(a//25,"x 25c")
    
b = a - (a//25)*25    
if b//10 != 0:
    print(b//10,"x 10c")
    
c = b - (b//10)*10    
if c//5 != 0:
    print(c//5,"x 5c")
    
d = c - (c//5)*5
if d//1 != 0:
    print(d//1,"x 1c")

    
    