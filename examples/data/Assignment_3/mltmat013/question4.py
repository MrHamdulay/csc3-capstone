begn = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def palindrome(start,stop):
    for i in range(start+1,stop):
        if str(i) == str(i)[::-1]:
            k = 1
            multiples = 0
            while k <= i:
                if i%k == 0:
                    multiples += 1
                    k += 1
                else:
                    k +=1
            if multiples == 2:
                print(i)                       
palindrome(begn,end)