#Promgram to find the palendrom primes
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(n+1,m):
                for j in range(2,i):
                                if i%j==0:break
                else:
                                if str(i)==str(i)[::-1]:
                                                print(i)
                                else: continue        
      

            
         
       
            
            
            
