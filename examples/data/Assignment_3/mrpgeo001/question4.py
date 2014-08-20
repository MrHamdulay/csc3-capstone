start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range(start + 1,end):
    if i%2 == 0 and i != 2:
        continue
    elif i%3 == 0 and i != 3:
        continue
    elif i%5 == 0 and i != 5:
        continue
    elif i%7 == 0 and i != 7:
        continue
    elif i%11 == 0 and i != 11:
            continue 
    elif i%13 == 0 and i != 13:
            continue
    elif i%17 == 0 and i != 17:
            continue    
    else:
        original = str(i)
        reverse = str(i)
        reverse = reverse[::-1]
        if reverse == original:
            print(i)
    
            
    