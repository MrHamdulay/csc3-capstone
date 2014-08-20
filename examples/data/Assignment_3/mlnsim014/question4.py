#program to find palindromic primes
#assignment3, question4
#Smanga

startPoint = eval(input("Enter the starting point N:\n"))
endPoint = eval(input("Enter the ending point M:\n"))
factorCount = 0

print("The palindromic primes are:")

for i in range(startPoint+1,endPoint):
    reverse = str(i)[len(str(i))::-1]
    if reverse == str(i):
        for j in range(1,i+1):
            if i%j==0:
                factorCount+=1
                
        if factorCount<=2:
            print(i)
    factorCount=0
            

            