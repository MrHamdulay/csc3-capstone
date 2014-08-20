import math 
a = eval(input("Enter the starting point N:\n"))
b = eval(input("Enter the ending point M:\n"))


print("The palindromic primes are:")
for i in range(a+1,b):
    sumFactor = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            sumFactor+=1
            break
            
            
    if sumFactor==0:
        revStr = str(i)[len(str(i))::-1]
        if(str(i)==revStr):
            print(i)
        
    
        
