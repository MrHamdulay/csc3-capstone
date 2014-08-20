import math
def prime():
    x=eval(input("Enter the starting point N:\n"))
    y=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(x+1,y):
        #if i%2==0:continue
        i=str(i)
        rev_i=i[::-1]
        #print(rev_i)
        if rev_i==i:
            rev_i=int(rev_i)
            for n in range(2,rev_i-1):
                if rev_i%n==0:
                    break
            else:
                print(rev_i)
        i=int(i)
        
            
            

prime()