#emile mclennan
#A3
#Q4

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
flag = False
print("The palindromic primes are:")

for i in range(N+1,M):
     if i==2:
          print(i)
     for i2 in range(2,i):
          if i%i2==0: 
               flag = False
               break
          else:
               flag = True
     if flag == True:
          if str(i) == str(i)[::-1]:
               print(i)
     flag=False
                   
               