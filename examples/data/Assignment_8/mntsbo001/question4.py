"""Program to determine palindromic primes
Sbonelo Mntungwa
9 May 2014"""

import sys                                          #for recursion limits
sys.setrecursionlimit (30000)

start = input("Enter the starting point N:\n")      #Inputing variables
end = input("Enter the ending point M:\n")
if start== '' and end == '':                        #Case for empty strings
    nothing = "nothing"                             #Breaking program
else:
    print("The palindromic primes are:")
    def main(start,end):                            #Defining main function of program 
        start = int(start)                          # making variables into integers
        end = int(end)
            
        start_pali = str(start)                     #Assigning variable start_pali
        if end>=start:                              # When end value is the same or greater than start value
            def palindrome(start,start_pali):       #defining function to see if number is a palindrome
                start_prime = 2
                if (len(start_pali) == 0 or len(start_pali) == 1):
                    def prime(start_prime):         #Defining function to see if number which is a palindrome is also a prime number
                        if start_prime == start:
                            print(start)            #printing final output
                    
                                                 
                        else:
                            if start_prime < start:
                                if start%start_prime!= 0:                                    
                                    return prime(start_prime+1)#adding variable start_prime by one till variable is equal to the start variable
                    prime(start_prime)              #Calling prime function
                else:
                    if start_pali[0] == start_pali[-1]:
                        return palindrome(start,start_pali[1:-1])#slicing variable start_pali till length of variable is 1 or 0
            palindrome(start,start_pali)  #calling function palindrome          
            return main(start+1,end) #Addind variable start by one till it is greater than the end variable

            
    main(start,end)            #Calling function main