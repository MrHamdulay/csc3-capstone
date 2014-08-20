def pal_prime():
    start = eval(input("Enter the starting point N: \n"))
    end = eval(input("Enter the ending point M: \n"))
    #start+= 1   
    print("The palindromic primes are:")
    if start<=1:
        print("2")
    
    for i in range(start+1,end):
        if(str(i) == str(i)[::-1]): #this gives me all numbers that are palindromes in range of input
            if(i>2): 
                for start in range(2,i):        #loop to check if primes
                    pal = True
                    if(i%start==0):
                        pal = False
                        break              
                if pal:                  #remember to line up this "if" with the second "for"!!!!!(or it just repeats numbers...)
                    print(i)
pal_prime()                        