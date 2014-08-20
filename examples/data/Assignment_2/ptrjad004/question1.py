#Jade Petersen
#Assignment 2_question 1
#14 March 2014

def main():
   year = eval(input("Enter a year:\n"))
  
   if (year%400==0) or (year%4==0) and (year%100 != 0):
      print(year,"is a leap year.")
   
   else:
      print(year,"is not a leap year.")

main()
