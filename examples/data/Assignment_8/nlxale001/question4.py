#Author: NLXALE001
#Date: 6 May 2014
#Assignment8

import sys
sys.setrecursionlimit (300000)

global n
n = input("Enter the starting point N:\n")
global m
m = int(input("Enter the ending point M:\n"))
global pos
pos = 0
global indexbegin
indexbegin = 0
global primenum 
primenum = []
testnum = ""
global indexend
indexend = len(testnum)-1
global test
test = eval(n)-1
global count
count = 1


def checkprime(n, test, primenum):
        n = int(n)
        
        #check if number % test value is 0 or not
        #test if we have entered the end of the list for the range of numbers and if not print next
        if n <= m:  
                if test==1: 
                        primenum.append(n)
                        n += 1
                        checkprime(n, n-1, primenum)
                elif test==0: #to avoid dividing by zero in the next statement
                        n += 1
                        checkprime(n, n-1, primenum)                        
                elif n % test == 0: #is not a prime number
                        n += 1
                        checkprime(n, n-1, primenum)
                else: 
                        test -= 1
                        checkprime(n, test, primenum)
        

#fix indexend - starting as -1 want to start as appropriate number
def palin(indexbegin, indexend, primenum, pos, count, testnum):
        if pos < len(primenum)-1:
                        testnum = str(primenum[pos])        
        if count == 1:
                indexend = len(testnum)-1
                count == 2
        if pos <= len(primenum)-1:
                testnum = str(primenum[pos]) 
                #test if we have reached the middle and pali us still true
                if indexbegin == indexend:
                        print (testnum)
                        pos += 1
                        count == 1
                        palin(0,0, primenum, pos, count, testnum)
                        #test if pali remains to be true
                elif testnum[indexbegin]==testnum[indexend]:
                        count == 2
                        palin(indexbegin+1, indexend-1, primenum, pos, count, testnum)
                #end recursion
                else:
                        pos += 1
                        count == 1
                        palin(0,len(testnum)-1, primenum, pos, count, testnum)

print ("The palindromic primes are:")                        
checkprime(n, test, primenum)
palin(indexbegin, indexend, primenum, pos, count, testnum)

        