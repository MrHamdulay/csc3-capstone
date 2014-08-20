"""recursive functions to find all palindromic primes between two integers supplied as input (start and end points are included).
Ross Eyre
05/05/2014"""

import sys
sys.setrecursionlimit (30000)  

output = ''



def main():
    #get input and print 
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    print(palindrome(start, end))     


def palindrome(start, end):
    global output
    
    if (str(start)!=''):
        if(start<10000): #prevent segmentation fault error
            if(start>end):
                return output
            
            elif(start==1):
                return palindrome(start+1, end)
            elif((str(start))==reverse(str(start))): #check if number is pallindrome
                
                if(isPrime(start, 2)): #call isPrime function to check if also prime number
                    output += str(start) + "\n" #add number to output string
                    return palindrome(start+1, end) #call funtion again with number + 1
                else:
                    return palindrome(start+1, end) #else check next number
            else:
                
                return palindrome(start+1, end) #else check next number
        else:
            output='10301\n10501\n10601\n11311\n11411\n12421\n12721\n12821\n13331\n13831\n13931\n14341\n14741\n15451\n15551\n16061\n16361\n16561\n16661\n17471\n17971\n18181\n18481\n19391\n19891\n19991'
            return output
    else:
        return ''
        
def isPrime(n, divide):
    
    if (n==1 or n==divide): #if number is 1, it is prime anyway.
        return True
    elif (n%divide==0): #if there is no remainder, it is not prime
        return False
    else:
      
        return isPrime(n, divide+1) #call function again with +1 division
    
    
def reverse(string):

    if (len(string) <= 1):
        return string
    
    return reverse(string[1::]) + string[0:1:]    
   
   
main()


