def reverse(number):
    i = 0
    palin = 0
    while (number >= 10**i):
        digit = number%10
        palin = 10*palin + digit
        number = (number - digit)/10
    return palin

def ispalindrome(number):
    return (number == reverse(number))

def isprime(number):
    prime = False
    max_div = number // 2
    for i in range(2, max_div + 1, 1):
        if (number%i == 0): break
    else:
        if (number == 1):
            prime = False
        else: prime = True
    return prime

if __name__ == "__main__":
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(start+1, end, 1):
        if (ispalindrome(i)) and (isprime(i)):
            print(i)