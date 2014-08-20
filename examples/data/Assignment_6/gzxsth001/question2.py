"""A Programme to do basic vector calculations
Sthabiso Andile Gazu
April 2014"""
#ask for vectors
vector_A=input("Enter vector A:\n")
x=vector_A.split(" ")

vector_B=input("Enter vector B:\n")
y=vector_B.split(" ")
import math
#calculations
eq1=(int(x[0])+int(y[0]))
eq2=(int(x[1])+int(y[1]))
eq3=(int(x[-1])+int(y[-1]))#FOR A+B
print("A+B = [",eq1,','," ",eq2,','," ",eq3,"]",sep="")
eq1=(int(x[0])*int(y[0]))
eq2=(int(x[1])*int(y[1]))
eq3=(int(x[-1])*int(y[-1]))#FOR A*B
print("A.B =",eq1+eq2+eq3)
k=math.sqrt((int(x[0])**2+(int(x[1]))**2+(int(x[-1]))**2))
print("|A| =",'{0:.2f}'.format(k))
s=math.sqrt((int(y[0]))**2+(int(y[1]))**2+(int(y[-1]))**2)
print("|B| =",'{0:.2f}'.format(s))

