def main():
     x=eval(input("Enter the hours:\n"))
     y=eval(input("Enter the minutes:\n"))
     z=eval(input("Enter the seconds:\n"))
     
     if (x<0 or y<0 or z<0 or x>23 or y>59 or z>59):
          print("Your time is invalid.")
     elif (x>=0 and y>=0 and z>=0):
          print("Your time is valid.")
     elif (x<=23 and y<=59 and z<=59):
          print("Your time is valid.")
main()