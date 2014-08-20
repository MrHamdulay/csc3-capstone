# Assignment 2 - Question 1
# Tashiv Sewpersad
# 03 - 08 - 2014

# declarations
def main():
  iYear = eval(input("Enter a year:\n"))
  if (iYear % 400 == 0) or ((iYear % 4 == 0) and (iYear % 100 != 0)):
     print(iYear,"is a leap year.")
  else:
     print(iYear,"is not a leap year.")   


# live code
main()