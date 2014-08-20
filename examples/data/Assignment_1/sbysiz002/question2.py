#name: Sizwe Sibiya
#date: 25/02/2014
#student n.o: SBYSIZ002
#Assignement 1

x=eval(input("Enter the hours:\n"))
y=eval(input("Enter the minutes:\n"))
z=eval(input("Enter the seconds:\n"))

if 0<x<=24 and 0<y<=59 and 0<z<=59:
    print("Your time is valid.")
else :
    print("Your time is invalid.")