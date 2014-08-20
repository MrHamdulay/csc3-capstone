
#STUDENT NUMBER:BDHSAN003
def Pripalindrome():
      import math
      Beg=eval(input("Enter the starting point N: \n"))
      end=eval(input("Enter the ending point M: \n"))
      print("The palindromic primes are:")
      l=1
      
      for i in range(Beg+1,end):
            tnumb=Beg+l
            tstring=str(tnumb)
            if all(i%k!=0 for k in range(2,int(math.sqrt(i))+1)):
                  if(tstring==tstring[::-1]):
                        print(tstring)
                
            l+=1

Pripalindrome() 


    
    
    
    
    