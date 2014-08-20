 #Shaaheen Sacoor SCRSHA001
 #Program to find palidromic primes
 # 8 may 2014
import sys
sys.setrecursionlimit (30000)



def check_palindrome(s): #Checks if palindrome
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return check_palindrome(s[1:-1])
        else:
            return False
i = [2]
def check_prime(x): #Checks if number is a prime
    if x == 0:
        return False
    elif x == 1:
        return False
    elif x == 2:
        return True
    elif x % i[0] == 0 and i[0] < x:
        i.pop(0) 
        i.append(2)
        return False
    elif x % i[0] != 0 and i[0] < x:
        i.append(i[0] + 1)
        i.pop(0)
        return check_prime(x)
    elif x % i[0] == 0 and (x == i[0]):
        i.pop(0)
        i.append(2)
        return True
   
    
def palindrome_prime (start,finish): # Joins two functions to 
    if check_palindrome(str(start)) is True: #check palindrome
        if check_prime(start) is False:      #primes
            if start <=finish:       
                return palindrome_prime(start+1,finish)
        else:
            if start <=finish:
                palindrome_list.append(start)
                return palindrome_prime(start+1,finish)
    else:
        return palindrome_prime(start+1,finish)
    
def print_palindrome_list(i):
    if palindrome_list ==[]:
        return
    else:
        print(palindrome_list[i])
        if i != (len(palindrome_list)-1):
            return print_palindrome_list(i+1)
        
start = eval(input("Enter the starting point N:\n"))
finish = eval(input("Enter the ending point M:\n"))
palindrome_list =[]
palindrome_prime (start,finish)
print("The palindromic primes are:")
print_palindrome_list(0)