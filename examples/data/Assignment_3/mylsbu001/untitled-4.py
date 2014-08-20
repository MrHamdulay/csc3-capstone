import math
lowerNumber = eval(input("Enter lower value:\n"))
upperNumber =  eval(input("Enter upper value:\n"))
change=""
print("The pelindromes are:")
for i in range(lowerNumber,upperNumber):
      if(i%2!=0):       
            count=0
            b=2
            while(i>b):
                  if(i%b ==0):
                        count=count+1
                  b+=1
            if(count<2):
                  change = str(i)
                  change2=change[len(change)::-1]
                  if(change2==change):
                        print(change2)
            
     