import math
def main():
    x= eval(input("Enter the starting point N:\n"))
    y= eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    factor=0
    for i in range(x+1,y):
        primes= str(i)
        palindromic = primes[::-1]
        if palindromic == str(i):
            for g in range(1,i):
                if i%g==0:
                    factor=factor+1
                    
            if factor<2:
                print(i)
            factor=0
main()
            
            
              