def main():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    
    for i in range(N+1,M):
        p = str(i)
        k = p[::-1]
        if p == k:
            for j in range(2,M):
                if i==j:
                    print(i)
                else:
                    if i%j == 0:
                        break
                


main()