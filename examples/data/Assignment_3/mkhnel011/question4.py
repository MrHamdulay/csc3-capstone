#Question 4
#Assignment 3
#def prime_pali():
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(N+1,M):
        rvs=str(i)[::-1]
        rvs=int(rvs)
        
        if i==rvs:
                if i==2:
                        print(i)
                elif i==3:
                        print(i)
                if i%2!=0:
                        divisor = 2
                        for divisor in range(2,(i//2) + 1):
                                if i%divisor == 0:
                                        break
                        if divisor == (i//2):
                                print(i)
                        if i==1:
                                continue

#prime_pali():
        #print(i
        #if i%2==0:
            #continue
        #else print(i)
        #for divisor in range(2,sqrt(i)+1):
           # print(i/divisor)
          