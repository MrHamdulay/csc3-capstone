height = eval(input("Enter the height of the triangle:\n"))
n = height - 1 
count = 0
for i in range(height):
    print(n *" " + (count + 1) * "*" + n *" ")
    count = count + 2
    n = n - 1
    
    
    
    