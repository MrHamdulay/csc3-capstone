import math 

vectorAValues=(input("Enter vector A:\n")).split(" ")
vectorBValues=(input("Enter vector B:\n")).split(" ")

def sum(a,b):
    sumValues=[]
    for i in range(3):
        sumValues.append(int(a[i])+int(b[i]))
    print ("A+B =",sumValues)
    
#Amitha Doodnath
#DDNAMI001
#23/04/2014
#Programme to do vector calculations

def product(a,b):
    product=0
    for i in range(3):
        product+=(int(a[i])*int(b[i]))
    print("A.B =",product)
    
def norm(v,a):
    sum=0
    for i in range (3):
        sum+= int(a[i])**2
    result="{0:.2f}".format(math.sqrt(sum))
    print("|",v,"| = ",result,sep="")
    
sum(vectorAValues,vectorBValues)
product(vectorAValues,vectorBValues)
norm("A",vectorAValues)
norm("B",vectorBValues)