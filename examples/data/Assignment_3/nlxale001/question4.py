#Author: NLXALE001
#Date: 27 March 2014
#Assignment 3

nstart = eval(input("Enter the starting point N:\n"))
mend = eval(input("Enter the ending point M:\n"))
print ("The palindromic primes are:")
start = nstart+1
end = mend

for n in range(start, end):
        primepali = False
        #check if palindrome
        m = n
        a = 0
        while(m!=0):
                a = m % 10 + a * 10
                m = m // 10
                if( n == a):#number is palindrome
                        for j in range(2,n):
                                if (n % j) > 0:
                                        primepali = True
                                else: 
                                        primepali = False
                                        break
                if n==2:
                        primepali = True                
                if primepali == True:                
                        print (n)

                
                
                