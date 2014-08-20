#Shahrain Coovadia
#CVDSHA002


s=int(input("Enter the starting point N:\n"))
e=int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
r= s+1
def Palindrome(x):
                    for i in range (len(str(x))):
                                        back=str(x)[::-1]
                    if(back==str(x)):
                                        print(back)
while (r<e):
                    if(r==0 or r==1):
                                        r+=1
                    if(r==2):
                                        Palindrome(2)              
                    else:    
                                        for i in range(2, r):
                                                            if r % i == 0:
                                                                                break        
                                        else:
                                                            Palindrome(r)
                                
                                
                    r+=1   
                    