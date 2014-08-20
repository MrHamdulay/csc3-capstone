# * Triangle
# Sofia Palmer
# 24/3/14

height = eval(input("Enter the height of the triangle: \n"))
x = height - 1
for i in range(1,height+1):
   line = " " * x + "*" * (2*i-1)
   x = x - 1
   print(line)
    
    

    