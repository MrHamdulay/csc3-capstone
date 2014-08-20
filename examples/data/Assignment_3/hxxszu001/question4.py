start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))

start +=1 
print("The palindromic primes are:")
                    
for i in range(start,end):
        y = True
        if(str(i) == str(i)[::-1]):
                if(i>2):
                        for a in range(2,i):
                                if(i%a==0):
                                        y = False
                                        break
                        if y:
                                print(i)