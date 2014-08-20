#HLNSIB005: Sibulele Hlongwane
start=eval(input("Enter the starting point N:\n"))
stop= eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
for i in range(start+1,stop):                     #i=202
        reverse= (str(i)[::-1])
        if reverse==str(i):
                for j in range(2,i):        #j= 200, 202......but...#j=2
                        if i%j==0:
                                break
                else:
                        print(i) 
        else:
                continue
                        
       