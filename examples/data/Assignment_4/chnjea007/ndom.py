# assignment 4 question 2
def decimal_to_ndom (a):
    return (a // 36 * 100) + (a % 36 // 6 * 10) + (a % 36 % 6)
def ndom_to_decimal (a):
    return (a // 100 * 36) + (a % 100 // 10 * 6) + (a % 100 % 10)
def ndom_add(a, b):
    thirty_sixes = (a + b) // 100
    thirty_sixes = (thirty_sixes % 6 * 100) + (thirty_sixes // 6 * 1000) # finds value of 6^2 with remainder from 6^1 included - repeats in function for 6^1 and 6^0
    sixes = (a + b) % 100 // 10
    sixes = (sixes % 6 * 10) + (sixes // 6 * 100) 
    digits = (a + b) % 100 % 10
    digits = (digits % 6) + (digits // 6 * 10)
    return thirty_sixes + sixes + digits
def ndom_multiply (a, b):
    a = [a % 100 % 10, a % 100 // 10, a // 100]
    b = [b % 100 % 10, b % 100 // 10, b // 100]
    remainder = 0
    temp = 0
    answer = 0
    for i in range (3):
        for j in range (3):
            temp = temp + ((a[i] * b[j] + remainder) % 6 * 10**j)
            remainder = a[i] * b[j] // 6
        temp *= 10 ** i
        answer = ndom_add(answer, temp)
        temp = 0
    answer += remainder * 1000
    return answer