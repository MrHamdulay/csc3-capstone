import math

a = 2
term = a
function = term
strin = ""
i=1

while (term>1):

        strin = "+ math.sqrt(a "*i + ")"*i
        term = a/eval(strin) 
        function = function * term 
        i = i +1
           
pi = round(function,3) 
print("Approximation of pi:",pi)
radius = eval(input("Enter the radius:\n"))
area = function*radius**2 
print("Area:",round(area,3))