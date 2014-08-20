starting = eval(input("Enter the starting point N:\n"))
ending = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(starting + 1, ending):
    if(str(i) == str(i)[::-1]):
        palindrome = i
        count = 0
        for j in range(ending ):
            remainder = palindrome % (j + 1)
            if(remainder == 0):
                count = count + 1
        if(count == 2):
            print(str(palindrome))
            
     
                