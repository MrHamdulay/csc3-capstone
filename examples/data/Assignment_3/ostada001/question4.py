def palindrome (num):
    return str(num) == str(num)[::-1]
    
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
if N<2:
    print(2)
N+=1

while N<M:
    if palindrome(N) == True:
        for i in range(1,N,1):
            if i>1 and i<N:
                if N%i != 0:
                    if i == N-1:
                        print(N)
                    else:
                        continue
                else:
                    break
    N+=1