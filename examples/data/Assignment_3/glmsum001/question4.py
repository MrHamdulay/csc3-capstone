def palind():
      import math
  
      start=eval(input("Enter the starting point N: \n"))
      
      end=eval(input("Enter the ending point M: \n"))


      print("The palindromic primes are:")

      counter=1
      
      
      for i in range(start+1,end):
    
            num=start+counter

            numString=str(num)
        
            if all(i%k!=0 for k in range(2,int(math.sqrt(i))+1)):

                  if(numString==numString[::-1]):

                        print(numString)
                
            counter+=1


palind() 


    
    
    
    
    