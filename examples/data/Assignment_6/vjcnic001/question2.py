'''Vector program
Nicol Vojacek'''
import math
import decimal
list_a = []
list_b = []
list_sum = []
list_prod = [] 


a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

for thing in a.split(" "): 
	list_a.append(thing) #inset input to list

for other_thing in b.split(" "): 
	list_b.append(other_thing)
	
for t in range(len(list_a)):
	y = eval(list_a[t]) + eval(list_b[t]) #convert str to int and add both list numbers in same position
	list_sum.append(y) #return values to list

for p in range(len(list_a)):
	g = eval(list_a[p]) * eval(list_b[p]) #product of 2 numbers in list
	list_prod.append(g)
	
prod = 0
for o in list_prod:
	prod = prod + o #add products in above list
	

sum_a = 0	
for k in range(len(list_a)):
	 sum_a = sum_a + eval(list_a[k])**2 #raise each item in list to power of two and add together

a = (math.sqrt(sum_a)) #square root of above addition


sum_b = 0
for l in range(len(list_b)):
		sum_b = sum_b + eval(list_b[l])**2

b = (math.sqrt(sum_b))

print("A+B =",list_sum) #return 
print("A.B =",prod)
print("|A| =", "%0.2f"%(a))
print("|B| =","%0.2f"%(b))
