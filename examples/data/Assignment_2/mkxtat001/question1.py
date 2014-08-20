#Tato Moaki MKXTAT001
#Program to determine whether an input year is a leap year or not
#question1 Assignment2
def main():
  leapYear = eval(input("Enter a year:\n"))
  if (leapYear%400==0) or ((leapYear%4==0) and (leapYear%100 != 0)):
      print(leapYear,"is a leap year.")
  else:
      print(leapYear,"is not a leap year.")
main()