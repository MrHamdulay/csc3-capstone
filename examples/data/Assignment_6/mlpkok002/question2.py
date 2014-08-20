import math 

#get string of items for each vector:
A_string=input("Enter vector A:\n") 
B_string=input("Enter vector B:\n")

#convert string of items to lists of strings:
A=A_string.split(" ")
B=B_string.split(" ")

#convert list items to integers,since we are going to do calculations:             
A1=[]
for i in A:
    A1.append(eval(i))
B1=[]    
for i in B:
    B1.append(eval(i))
    
#can also use this:
#A=[int(i) for i in A]
#B=[int(i) for i in B]

#create empty lists:
Sum=[]
product=[]
powers_A=[]
powers_B=[]

#fill empty list for each calculation type:
for i in range(len(A1)):
    Sum.append(A1[i]+B1[i])    #sum the correspoding elements from the lists A1 and B1
    product.append(A1[i]*B1[i]) #multiply the correspoding elements from the lists A1 and B1
    powers_A.append(A1[i]**2) #square all values in A1. DO THE SAME FOR B1 THROUGHOUT
    powers_B.append(B1[i]**2)
print("A+B =", Sum)
    
product_sum=[]
for i in product:
    product_sum=sum(product) #add together the products of each A1[i]+B1[i], obtained from previous loop 
print("A.B =",product_sum)

sum_powers_A=[]
for i in powers_A:
    sum_powers_A=sum(powers_A) #sum the squares of A1, obtained from previous loop
sqrt_tot_A=math.sqrt(sum_powers_A) #square the sum of the squares

x=sqrt_tot_A
if sqrt_tot_A==0:
    print("|A| = 0.00")
else:
    print("|A| =", round(sqrt_tot_A,2))

sum_powers_B=[]
for i in powers_B:
    sum_powers_B=sum(powers_B)
sqrt_tot_B=math.sqrt(sum_powers_B)

y=sqrt_tot_B
if y==0:   
    print("|B| = 0.00") 
else:
    print("|B| =", round(sqrt_tot_B,2))


    
