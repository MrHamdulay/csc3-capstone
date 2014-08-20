start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
sumFactor = 0

print("The palindromic primes are:\n",end="")
for i in range(start+1,end):
    for j in range(1,i+1):
        if i%j==0:
            sumFactor +=1
            
    if sumFactor<=2:
        revStr = str(i)[len(str(i))::-1]
        if(str(i)==revStr):
            print(i)
        
    sumFactor = 0;
        
