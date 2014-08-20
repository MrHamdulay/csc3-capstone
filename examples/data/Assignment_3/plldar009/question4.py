begin = int(input("Enter the starting point N:\n"))

end = int(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

s= begin +1

def Prime(g):
                    for i in range (len(str(g))):
                                        back=str(g)[::-1]
                    if(back==str(g)):
                                        print(back)
while (s<end):
                    if(s == 0 or s == 1 ):
                                        s+=1
                    if(s == 2):
                                        Prime(2)              
                    else:    
                                        for i in range(2,s):
                                                            if s % i == 0:
                                                                                break        
                                        else:
                                                            Prime(s)
                                
                                
                    s+=1   
                    
