# assignment 3 question 4
def prime(num):
    prime = True
    for i in range (2, num//2 + 1):
        if num % i == 0:
            prime = False
            break
    return prime
def pal(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start + 1, end):
    if i == 1:
        continue
    if pal(i) == True:
        if prime(i) == True:
            print(i)