import math

x= eval(input("Enter the starting point N:\n"))
y= eval(input("Enter the ending point M:\n"))

for i in range(x+1,y):
    for j in range(2,round(math.sqrt(y)+1)):
        if i%j==0 : break
     
    else:
        if str(i)==str(i)[::-1]:
            print(i)
        
           
        

        