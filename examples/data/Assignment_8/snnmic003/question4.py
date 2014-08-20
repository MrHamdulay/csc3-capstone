import math
import sys
sys.setrecursionlimit (30000)

#Checks to see if the number is a palindrome
def palindrome (number):
    if len(number) < 2:
        return True
    elif (number [0] == number [-1]):
        return palindrome (number[1:-1])
    else:
        return False
#Checks to see if the number is a prime number
def prime (number, tester):
    if (tester > math.sqrt(number)):
        return True
    elif (number % tester == 0):
        return False
    else:
        return prime (number, tester+1)
#Runs the start to end number through the palindrome checker and the prime checker and prints the output if both are true
def main (start, end):
    if start <= end:
        if (start ==1):
            start+=1
            print (start)
        else:
            if (palindrome(str(start)) == True):
                if prime(start, 2) == True:
                    print (start)
        return main(start+1, end)
        
# Accepts the usres input into the program
start = eval (input("Enter the starting point N:\n"))
end = eval (input ("Enter the ending point M:\n"))
print ("The palindromic primes are:")
main (start, end)