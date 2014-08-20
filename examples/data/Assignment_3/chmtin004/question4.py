#Program to decorate messages
#Tinotenda Chemvura (CHMTIN004)
#24 March 2014

#____________________Program Starts Here_____________________*

srtN=eval(input("Enter the starting point N:\n"))
endM=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(srtN+1,endM,1):  
    fwd=str(i)
    rev=fwd[::-1]
    if fwd==rev:   
        for j in range(2,i,1):      
            if i%j==0:
                break
        else:
            print(fwd)

#_________________Program ends here_______________*