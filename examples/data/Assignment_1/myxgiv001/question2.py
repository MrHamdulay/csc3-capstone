def validitycheck():
      a=eval(input("Enter the hours:"'\n'))
      b=eval(input("Enter the minutes:"'\n'))
      c=eval(input("Enter the seconds:"'\n'))
      if a<0 or a>23:
            print("Your time is invalid.")
      elif b<0 or b>59:
            print("Your time is invalid.")
      elif c<0 or c>59:
            print("Your time is invalid.")
      else:print("Your time is valid.")
      
validitycheck()
      