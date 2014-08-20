import math

deno = math.sqrt(2)
pi = 4 / deno

while 2/deno > 1:
    deno = math.sqrt(2 + deno)
    pi*= 2/deno

x = round(pi, 3)
print("Approximation of pi: ",x, sep = "")

radius = eval(input("Enter the radius: \n"))
area = round((radius**2)*pi, 3)
print ("Area: ", area, sep = "")
