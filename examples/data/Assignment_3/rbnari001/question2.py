height = eval (input ("Enter the height of the triangle:\n"))
x = "**"
total = "*"
count = height - 1
while height != 0:
    total = total + x
    newtotal = total[:-2]
    print((count)*" "+newtotal)
    height = height -1
    count = height - 1
        