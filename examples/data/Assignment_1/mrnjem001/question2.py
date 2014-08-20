hours = input("Enter the hours:\n")
hours = eval(hours)
mins = input("Enter the minutes:\n")
mins = eval(mins)
secs = input ("Enter the seconds:\n")
secs = eval(secs)
x = 5
if -1<hours<24: x = 5
else: x = 2
if mins<0: x = 2
if secs<0: x = 2
if mins>59: x = 2
if secs>59: x = 2
if type(hours) != int: x = 2
if type(mins) != int: x = 2
if type(secs) != int: x = 2
if x == 5 : print("Your time is valid.")
else: print("Your time is invalid.")