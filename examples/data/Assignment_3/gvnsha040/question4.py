#PrimePalz
start = int(input("Enter the starting point N:\n"))

end = int(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

palindrome= start+1

def Palz(z):
                    for i in range (len(str(z))):
                                        back = str(z)[::-1]
                    if(back == str(z)):
                                        print(back)
while (palindrome < end):
                    
                    if(palindrome == 2):
                                        print(2)              
                    else:    
                                        for i in range(2, palindrome):
                                                            if palindrome % i == 0:
                                                                                break        
                                        else:
                                                            Palz(palindrome)
                                
                                
                    palindrome = 1 + palindrome   
                    
