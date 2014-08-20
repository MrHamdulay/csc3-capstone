y = eval(input("Enter a year:\n"))
divby400 = False
divby4 = False
notdivby100 = True
i = 0
while (4*i)<=y:
    if i*4 == y:
        divby4 = True
    if i*400 == y:
        divby400 = True      
    if i*100 == y:
        notdivby100 = False
    i= i+1
if (divby400) or ((divby4) and (notdivby100)):
    print (y, "is a leap year.")  
else:
    print (y, "is not a leap year.") 