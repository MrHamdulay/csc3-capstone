N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(N+1,M):
        string = str(i)
        reverse_string = string[::-1]
        if string == reverse_string:
                reverse = eval(reverse_string)
                prime = True
                for a in range(2,reverse):
                        if reverse % a == 0:
                                prime = False
                                break
                if prime == True:
                        print(reverse)