#Shahrain Coovadia
#CVDSHA002


start=int(input("Enter the starting point N:\n"))
end=int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
n= start+1
def Palindrome(s):
                    for i in range (len(str(s))):
                                        back=str(s)[::-1]
                    if(back==str(s)):
                                        print(back)
while (n<end):
                    if(n==0 or n==1):
                                        n+=1
                    if(n==2):
                                        Palindrome(2)              
                    else:    
                                        for i in range(2, n):
                                                            if n % i == 0:
                                                                                break        
                                        else:
                                                            Palindrome(n)
                                
                                
                    n+=1   
                    