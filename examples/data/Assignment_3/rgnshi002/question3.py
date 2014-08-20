x = input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))

l = len(x)

s = l + z*2 

c = 0

for i in range(z):
    print("|" * c + "+" + "-"*s + "+" + "|" * c)
    c += 1
    s -= 2
        
for i in range(y):      
    print("|"*z,x,"|"*z)
    
s += 2

c -= 1
    
for i in range(z):
    print("|" * c + "+" + "-"*s + "+" + "|" * c)
    s += 2
    c -= 1