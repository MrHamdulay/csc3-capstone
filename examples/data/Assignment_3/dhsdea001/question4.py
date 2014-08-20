#Question4 
#Determining the prime paladromes
#By: Dean de Haast
N= eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
prime = False


for i in range((N+1),M):
    i=str(i)
    pal=i[::-1]  
          
    if i==pal:
                      
        for x in range(2,M):
            i=int(i)
            if i!=x:
                if i%x ==0:
                    break
            else:
                print(i)                                           