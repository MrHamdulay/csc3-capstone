# question4.py
# bxtnaa002
# May 2014

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the starting point M:\n"))

def palin(n):
        if n == "":
                return n
        else:
                return palin(n[1:]) + s[0]
def palin_check(n):
        x = palin(n)
        if x == n:
                return True
        else:
                return False
count = 2
def prime(n,count):
        #global count
        
        if (n % count == 0) and (n < count):
                print(count)
                return True
        if (n >= count):
                count=count+1
                return prime(n,count)

#def palin_prime(n+1, m):
print(prime(n,count))