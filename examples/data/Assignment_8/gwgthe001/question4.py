#Thembekani Gwegwana
# A program to find palindromic primes between two supplied numbers
#May 2014
import sys
sys.setrecursionlimit (30000)


#A fuction to check whether or not a number is a palindrome
def palindrome(string_no):
    if len(string_no) <= 1 :
        return ' Palindrome'
    else :
        if string_no[0] == string_no[len(string_no)-1]: 
            return palindrome(string_no[1:len(string_no)-1])
        else:
            return False

# A function to check whether or not a number is a prime   
def prime_numbers (start_point, end_point):
    if (end_point>start_point**(1/2)):
        return True
    if start_point%end_point == 0 : #a prime number is only divisible by itself
        return False
    else:
        return prime_numbers(start_point,end_point+1)

#A function to check whether a number is a palindrome and a prime number
def palindro_primes(start_point,end_point):
    if start_point> end_point:
        return
    else :
        if palindrome(str(start_point)) and prime_numbers(start_point,2):
            print(start_point)
        palindro_primes(start_point+1, end_point)

start_point =eval(input('Enter the starting point N:\n'))
if start_point == 1 :
    start_point+=1
end_point= eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
palindro_primes(start_point,end_point)