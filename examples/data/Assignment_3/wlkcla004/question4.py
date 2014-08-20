N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1, M):
    if i==2:
        print(i)
        continue
    r=str(i)[::-1]
    if str(i)!=r:
        continue
    if str(i) == r:
        import math
        end=math.sqrt(i)+1
        end2=int(end)         
        for j in range(2, end2+1):
            if j == end2:
                if i%j != 0:
                    print(i)
                else:
                    break
            if i%j !=0:
                continue
            else:
                break
        
    
