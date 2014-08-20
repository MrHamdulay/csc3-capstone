begin=eval(input("Enter the starting point N:""\n"))
finish=eval(input("Enter the ending point M:""\n"))
print("The palindromic primes are:")
for i in range(begin+1,finish):

    if all(i%k!=0 for k in range(2,i)):

        if str(i) == str(i)[::-1]:

            print(i)