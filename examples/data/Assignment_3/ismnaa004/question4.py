start =eval(input("Enter the starting point N:\n"))
end =eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for num in range(start,end):
    if(str(num) == str(num)[::-1]):
        if(num>2):
            for start in range(2,num):
                y = True
                if(num%start==0):
                    y = False
                    break
            if y:
                print(num)