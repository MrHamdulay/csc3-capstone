#Raeesa Behardien
#BHRRAE003
#Assignment 3 - 28 March 2014

#Question 4
#Program to find palindromic primes between two integers

N=eval(input("Enter the starting point N:" '\n')) 
M=eval(input("Enter the ending point M:" '\n'))

def pal():
    for i in range ((N+1),M):
        i=str(i)
        revi=i[::-1]
        if i==revi: 
            for x in range(2,M):
                if int(i)!=x:
                    if int(i)%x==0:
                        break
                else:
                    print(i)
                    
print("The palindromic primes are:")
pal() 
    
