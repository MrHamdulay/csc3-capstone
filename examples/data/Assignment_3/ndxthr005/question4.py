def palindromes():
      import math
  #input
      beg=eval(input("Enter the starting point N: \n"))
      end=eval(input("Enter the ending point M: \n"))
      print("The palindromic primes are:")
      count=1
      
  #processing -- output    
      for i in range(beg+1,end):
    
            num=beg+count
            numS=str(num)
        
            if all(i%k!=0 for k in range(2,int(math.sqrt(i))+1)):
                  if(numS==numS[::-1]):
                        print(numS)
                
            count+=1

palindromes() 


    
    
    
    
    