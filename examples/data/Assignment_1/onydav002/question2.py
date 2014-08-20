# Time

t = eval(input("Enter the hours:\n"))
u = eval(input("Enter the minutes:\n"))
v = eval(input("Enter the seconds:\n"))

if(t>=0 and t<=23) and (0<=u and u<=59) and (0<=v and v<=59):
    print("Your time is valid.")   
else :
    print("Your time is invalid.")