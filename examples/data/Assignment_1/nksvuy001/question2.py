#program to check validity of a time entered by user as a set of three integers
#vuyolwethu nkosi
#3 march 2014

a=eval(input("Enter the hours:\n"))
b=eval(input("Enter the minutes:\n"))
c=eval(input("Enter the seconds:\n"))
if(0<=a<=23):
      if(0<=b<=59):
            if(0<=c<=59):
                  print("Your time is valid.")
            else:
                  print("Your time is invalid.")    
      else:
            print("Your time is invalid.")
else:
      print("Your time is invalid.")
  