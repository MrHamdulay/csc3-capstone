startingPoint=eval(input("Enter the starting point N:\n"))endingPoint=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for x in range (startingPoint+1,endingPoint):
                for y in range (2,x):
                                if x%y==0: break
                else:                                string=str(x)                                reverseString=string[::-1]                                if string==reverseString:                                                print(string)                                                                                

                                       
                                       
                               