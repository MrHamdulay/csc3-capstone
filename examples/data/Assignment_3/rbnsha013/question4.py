print("Enter the starting point N:")
N = eval(input())
print("Enter the ending point M:")
M = eval(input())
print("The palindromic primes are:")
count = N
while count<M-1:
     count+=1
     for i in range(2,count):
               if count%i==0:
                    break
     else:
          if str(count)==str(count)[::-1]:
               print(count)