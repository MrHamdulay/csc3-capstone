def isPrime(number, minimum):
    bFlag = True
    checkNumber = number
    while (checkNumber > minimum):
        checkNumber -= 1
        i = number // checkNumber
        if (type(i) == int):
            bFlag = False
            break
        return bFlag

def isPalandrome(number):
    string1 = str(number)
    string2 = string1[::-1]
    
    if (string1 is string2):
        return True
    else:
        return False
    

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:\n")
for i in range(N+1,M):
    if ((isPrime(i, N)) and (isPalandrome(i))):
        print(i)

    