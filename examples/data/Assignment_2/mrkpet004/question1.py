x = eval(input("Enter a year:\n"))
remainder = x % 400
remainder1 = x % 4
remainder2 = x % 100

if (remainder == 0) or (remainder1 == 0) and (remainder2 > 0): 
    print (x,"is a leap year.")
else:
    print (x,"is not a leap year.")
        