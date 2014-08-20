#CHTTEVOO1
#Assignment 3
#Question 4

n=eval(input("Enter the starting point N: \n"))
m=eval(input("Enter the ending point M: \n"))
print("The palindromic primes are: ")

if n <2: 
    print (2)
for i in range (n+1,m,1):
    x=str(i)
    if x==x[::-1]:
        x=int(x)
        for j in range (2,x):
            if x%j==0:
                break

            elif j==(x-1):
                print(x)
                
            
                
                
                
                #count+=1
                
                #if count==2:
                    #break
            #else: print(x)
                    

            
            