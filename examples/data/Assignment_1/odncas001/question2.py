def time_valid(h,m,s):
    if h >= 0 and h <= 23:
       if m >= 0 and m <= 59:
          if s >= 0 and s <= 59:
             print("Your time is valid.")
          else: print("Your time is invalid.")
       else: print("Your time is invalid.")
    else: print("Your time is invalid.")
    
h = eval(input("Enter the hours:\n"))
m = eval(input("Enter the minutes:\n"))
s = eval(input("Enter the seconds:\n"))
time_valid(h,m,s)
       