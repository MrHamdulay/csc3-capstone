start = eval(input("Enter the starting point N: \n"))
end = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")

a=1
for i in range(start+1, end, 1):
     for d in range(2,i,1):
          if i%d==0:
               a=1
               break
          else: a=2
     if a==2:
        reverse = int(str(i)[::-1])
        if reverse == i:
             print(i)
     if i==2: print(i)