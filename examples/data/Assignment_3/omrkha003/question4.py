# program to find all primes between two integers supplied
# 25 March 2014
# by: khadeejah omar

start = eval(input("Enter the starting point N: \n"))
end = eval(input("Enter the ending point M: \n"))
z = start + 1

print("The palindromic primes are:")

def Palindrome(x):
                    for i in range (len(str(x))) :
                                        y = str(x)[::-1]
                    if y == str(x) :
                                        print(y)
while z < end:
                    if z == 0 or z == 1 :
                                        z = z + 1
                    if z == 2 :
                                        Palindrome(2)              
                    else:    
                                        for i in range(2, z):
                                                            if z % i == 0 :
                                                                                break        
                                        else:
                                                            Palindrome(z)
                                
                                
                    z = z + 1   
                    
    