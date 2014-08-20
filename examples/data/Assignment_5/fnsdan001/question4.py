import math
def roundInt(x):
    """iround(number) -> integer
    Round a number to the nearest integer."""
    if type(x)!=int:
        
        if (str(x)[0] =='0' and int(str(x)[2]) <5 ):
            return 0
        else:
            return int(round(x) - .5) + (x > 0)
    else:
        return x


func = input("Enter a function f(x):\n")
value = 0
cntspace= 0
for time in range(-10,11):
        
    for i in range (-10,11):
        value = eval(func.replace("x","i"))
        

        if roundInt(value) == -time:
            print("o", end = "" )
        elif i == 0 and time!=0:
            print("|", end = "")
        elif i==0 and time == 0:
            print("+", end = "")
        elif time == 0 and i!=0:
            print("-",end = "")
        else:
            print(" ", end = "")
    print()
    

        
