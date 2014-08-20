# Dean Gracey, GRCDEA001, assignment 3 question 1
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for numtocheck in range (start+1,end,1):
    for i in range(2,numtocheck,1):
        if (numtocheck%i==0):
            break
    else:
        #print(numtocheck, "prime") 
        pal = 1
        snumtocheck = str(numtocheck)
        for k in range(0,len(snumtocheck)-1,1):
            if (snumtocheck[k]==snumtocheck[len(snumtocheck)-1-k]):
                pal = pal
            else:
                break
            
        else:
            print(snumtocheck)
                
      
       
           
        
 