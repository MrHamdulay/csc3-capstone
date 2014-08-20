#Amitha Doodnath
#DDNAMI001
#24/03/2014
#Programme to find all palindromic primes in a user defined range

n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")


for i in range(n+1,m): #range of numbers excluding start and end points
    count=0
    prime=str(i) #convert prime number to string
    reverse= prime[::-1]
    if prime==reverse: 
        for j in range(i,0,-1): #checks if it is prime
                if i%j==0:
                    count+=1
        if count==2: #if it is prime        
            print(i)
        else:  continue
