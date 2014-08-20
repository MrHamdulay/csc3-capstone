start = eval(input("Enter the starting point N:\n"))

end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for num in range(start+1, end):
        if start ==end:
                break
                
        if all(num%i!=0 for i in range(2,num)):
                num = str(num) 
                if num=="1":
                        continue
                if num[::1] == num[::-1]:
                        print(num)                
               