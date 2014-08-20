import sys
sys.setrecursionlimit (30000)

def prime(X,Y):
    if Y<2:
        return False
    if X==Y:
        return True
    elif Y % X==0:
        return False
    else:
        return prime(X+1, Y)   
    
def Palindrome(string):
    if string == '':
        return True
    elif (ord(string[0]) == ord(string[len(string)-1])):
        return Palindrome(string[1:len(string)-1])
    else:
        return False

def check(N, M):
    if M+1==N:
        return ""
    else:
        if prime(2, N):
            if Palindrome(str(N)):
                print(N)
            return check(N+1, M)
        else:
            return check(N+1, M)
        
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
check(N, M)