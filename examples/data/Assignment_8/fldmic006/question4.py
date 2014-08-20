"""code to check if a group of numbers is prime and palindromic
Michael Field
5 May 2014"""
import sys
sys.setrecursionlimit (30000)

#sends each number within the bouns to the palin function to check if the 
def numbers(start, end, pos, count):
    num = eval(start) + count
    
    #make the function repeat with the values given
    if num <= eval(end):
        palindrome = palin(num, pos)
        
        #check if palindromic
        if palindrome == True:
            pcount = 3
            prime(num,pcount)
            count += 1
            numbers(start, end, pos, count)
        
        else:
            count += 1
            numbers(start, end, pos, count)
    
#checks if each number is a palindrome or not
def palin(num, pos):
    num = str(num)
    
    if pos == (len(num)-1):
        return True

    elif num[pos] == num[(len(num)-1-pos)]:
        pos += 1
        return palin(num, pos)
        
    else:
        return False
    
#checks if the number sent form the numbers function are prime or not
#print prime numbers, do nothing if not
def prime(num, pcount):
    #num = 1 which is not prime
    if num == 1:
        print("", end="")
    
    #2 is prime
    elif num == 2:
        print(num)
    
    #check if even
    elif num%2 == 0:
        print("", end="")
    
    elif pcount < int((num**0.5)+1):
        if num%pcount == 0:
            pcount+=2
            print("",end="")
        
        else:
            pcount += 2
            prime(num, pcount)
            
    elif (int(num**0.5)%2) == 0:
        if pcount == int((num**0.5)+1):
            print(num)
        
    elif (int(num**0.5)%2) != 0:
        if pcount == int((num**0.5)+2):
            print(num)          
        
    else:
        pcount += 2
        print("", end="")
            
#num = starting value; end = last number, pos = position, count = current number
start = input("Enter the starting point N:\n")
end = input("Enter the ending point M:\n")
pos = 0
count =  0
print("The palindromic primes are:")

numbers(start, end, pos, count)