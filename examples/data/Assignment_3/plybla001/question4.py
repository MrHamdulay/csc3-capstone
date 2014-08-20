#Prac 3 q4
#B.Player
#16/03/2014

s=eval(input("Enter the starting point N:\n"))
e=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(s+1,e):
        for j in range(2,i):
                if i%j!=0: continue
                break
        else:
                if(str(i)[::-1]==str(i)):
                        print(i)
    
     