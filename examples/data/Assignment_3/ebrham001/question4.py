import math



def Prime(N):
    N*=1.0
    for i in range(2,int(math.sqrt(N)+1)):
        if N/i==int(N/i):
            return False
    return True    
             
def Palindrome(x,y):
    for i in range(x,y):
        z = str(i)[::-1]
        if str(i) == z:
            if Prime(int(i)) == True:
                print(i)

def main():
    
    N=eval(input("Enter the starting point N:\n"))
    
    M=eval(input("Enter the ending point M:\n"))    
    
    
    print("The palindromic primes are:")
    Palindrome(N+1,M)
main()