number = eval(input("Enter a year:\n"))
divisor = 4
remainder = number%divisor

if remainder == 0 and number!= 2100: 
    print(number, "is a leap year.")
    
else: 
    print(number, "is not a leap year.")
