# Program to print out palindromic primes
# Nevarr Pillay - PLLNEV006
# 8 March 2014

def pal(num):
    newnum = str(num)   
    reverse = newnum[::-1]
    if(newnum == reverse):
        return True
    return False

def prime(num):
    for i in range(2,num):
        if (num%i==0):
            return False
    return True    

def main():
    start = eval(input("Enter the starting point N:\n")) + 1
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(start,end):
        if pal(i) == False:
            continue
        if(prime(i) ==  False):
            continue
        print(i)
    
    
main()  

