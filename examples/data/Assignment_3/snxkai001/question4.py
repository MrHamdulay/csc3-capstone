st = int(input("Enter the starting point N:\n"))

end = int(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

y= st+1

def Prime(y):
                    for i in range (len(str(y))):
                                        back=str(y)[::-1]
                    if(back==str(y)):
                                        print(back)
while (y<end):
                    if(y==0 or y==1):
                                        y+=1
                    if(y==2):
                                        Prime(2)              
                    else:    
                                        for i in range(2, y):
                                                            if y % i == 0:
                                                                                break        
                                        else:
                                                            Prime(y)
                                
                                
                    y+=1   
                    
