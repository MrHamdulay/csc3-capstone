# Question 2 - Assignment 6
# Oliver Harrison
# 21 April 2014



# Get vectors and add to list

a=[]
b=[]

a_input=input("Enter vector A:\n")
b_input=input("Enter vector B:\n")

for value in a_input.split(" "):
    a.append(value)

for value in b_input.split(" "):
    b.append(value)

# Calculate Addition

a_plus_b=[]

for index in range(3):
    x = eval(a[index]) + eval(b[index])
    a_plus_b.append(x)

print("A+B =",a_plus_b)
    
# Calculate Dot Product

a_times_b = 0

for index in range(3):
    a_times_b += (eval(a[index]))*(eval(b[index]))
    
print("A.B =", a_times_b)
    
# Calculate A Magnitude

sum_a = 0

for index in range(3):
    sum_a += (eval(a[index]))**2

a_mag = sum_a**(0.5)
print("|A| =","%0.2f"%round(a_mag, 2))

# Calculate B Magnitude

sum_b = 0

for index in range(3):
    sum_b += (eval(b[index]))**2

b_mag=sum_b**(0.5)
print("|B| =","%0.2f"%round(b_mag, 2))

                   

