#hours(h)
#minutes(m)
#seconds(s)

h=eval(input ("Enter the hours:\n"))
m=eval(input ("Enter the minutes:\n"))
s=eval(input ("Enter the seconds:\n"))

if(0<=s<=59)and(0<=m<=59)and(0<=h<=23):
            print("Your time is valid.")
else:    
            print("Your time is invalid.")