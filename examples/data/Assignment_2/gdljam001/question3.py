import math
botVal=math.sqrt(2)
termVal=2/botVal
pi=2
x=0
while(termVal!=1):
    
    termVal=2/botVal
    pi=pi*termVal
    botVal=math.sqrt(2+botVal)
    
print("Approximation of pi:", round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=(radius**2)*pi
print ("Area: "+str(round(area,3)))