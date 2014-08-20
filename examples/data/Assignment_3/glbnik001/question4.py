import math 
def prime(z):
    x=(int(z))
    z = "true"
    for y in range (2,x):
        if x%y==0:
            z = "false"
    if z == "true":
        print (x)
    
def main():
    s = eval(input("Enter the starting point N:\n"))
    e = eval(input("Enter the ending point M:\n"))
    print ("The palindromic primes are:")
    for i in range (s+1,e):
        if str(i)==str(i)[::-1]:
            prime(i)
main()

            
            