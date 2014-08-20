year = eval(input("Enter a year: \n"))

calc1 = year%400 
calc2 = year%4 
calc3 = year%100
if(calc1 == 0) or ((calc2 ==0) and (calc3 !=0)):
      print(year,"is a leap year.")
      
else:
      print(year,"is not a leap year.")