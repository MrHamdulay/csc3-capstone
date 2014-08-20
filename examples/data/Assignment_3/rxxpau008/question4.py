def prime(n):
    if n==2: return True
    if n%2==0: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    
    return True

def reverse(x):
    p = ''
    while x:
        x,p=x//10,p+str(x%10)
    return int(p)
        
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1,end,1):
    if prime(i) == True:
        if reverse(i)==i:
            print(i)