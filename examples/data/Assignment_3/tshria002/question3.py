

x = input("Enter the message:\n")

y = eval(input("Enter the message repeat:\n"))

z = eval(input("Enter the frame thickness:\n"))
b = len(x)

print("+"+"-"*(b+4)+"+")

for i in range(1,z):
    print("|"*i+"+-"+"-"*(b)+"-+"+"|"*i)
    z-=2
for i in range(y):
    z=z
    print("|"*z,x,"|"*z)
    
for i in range(1,z):
    print("|"*i+"+-"+"-"*(b)+"-+"+"|"*i)
    z-=2
print("+"+"-"*z+"-"*(b+4)+"-"*z+"+")
    
