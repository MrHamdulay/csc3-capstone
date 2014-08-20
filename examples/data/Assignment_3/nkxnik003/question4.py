#Nikhil Jiten Naik
#Question 4 - Assignment 3
#26 March 2014


beg=int(input("Enter the starting point N:\n"))
end=int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
t= beg+1
def testPal(x):
                    for i in range (len(str(x))):
                                        y=str(x)[::-1]
                    if(y==str(x)):
                                        print(y)
while (t<end):
                    if(t==0 or t==1):
                                        t+=1
                    if(t==2):
                                        testPal(2)              
                    else:    
                                        for i in range(2, t):
                                                            if t % i == 0:
                                                                                break        
                                        else:
                                                            testPal(t)
                                
                                
                    t+=1   
                    
               