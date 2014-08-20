def Palindrome_Generator():
    v_N = eval(input("Enter the starting point N:\n"))
    v_M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(v_N,v_M):
        j = str(i)
        k = j[::-1]
        if int(k) == i:
            b_prime = 1
            for l in range(2,v_M-1):
                if i%l == 0 and not l == i:
                    b_prime = 0
            if b_prime == 1 and v_N<i<v_M:
                print(i)
                    
Palindrome_Generator()
