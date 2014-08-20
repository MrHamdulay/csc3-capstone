start_point = eval(input("Enter the starting point N:\n"))
end_point = eval(input("Enter the ending point M:\n"))

def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for y in range(3, int(n**0.5)+1, 2):
        if n % y == 0:
            return False
    return True

print("The palindromic primes are:")

start_point = start_point + 1

while start_point < end_point:
    if str(start_point) == str(start_point)[::-1]:
        if prime(start_point) == True:
            print(start_point)
            start_point += 1
        else:
            start_point += 1
            continue 
    else: 
        start_point += 1
        continue