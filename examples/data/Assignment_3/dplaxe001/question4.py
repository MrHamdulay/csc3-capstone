start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
sumFactor = 0

print("The palindromic primes are:")

for i in range(start+1,(end)):
    if(i%10==0):
        continue
    iRevStr = str(i)[len(str(i))::-1]
    iRev = eval(iRevStr)
    if(i == iRev):
        for j in range ((i+1)):
            if(i%(j+1)==0):
                sumFactor = sumFactor + 1
        if(sumFactor <3):
            print(i)
    sumFactor = 0
        