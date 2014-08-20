m = int(input("Enter the starting point N:\n"))
n = int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
drome= m+1
def check(P):
                    for i in range (len(str(P))):
                                        reverse = str(P)[::-1]
                    if(reverse == str(P)):
                                        print(reverse)
while (drome < n):
                    if(drome == 0 or drome == 1):
                                        drome = drome + 1
                    if(drome == 2):
                                        check(2)              
                    else:    
                                        for i in range(2, drome):
                                                            if drome % i == 0:
                                                                                break        
                                        else:
                                                            check(drome)
                                
                                
                    drome = 1 + drome   
                    
