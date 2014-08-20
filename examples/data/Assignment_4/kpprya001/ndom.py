def ndom_to_decimal(a):
     
   stra = str(a)
   finalNum=0
   
   
   if (len(stra)==1):
      firstNum = eval(stra)
      finalNum =firstNum * 1
      
      
   if (len(stra)==2):
      firstNum = eval(stra[1:2])
      secondNum = eval(stra[0:1])
      finalNum = firstNum *1 + secondNum *6
      
      
   if (len(stra)==3):
      firstNum = eval(stra[2:3])
      secondNum = eval(stra[1:2])
      thirdNum = eval(stra[0:1])
      finalNum = firstNum *1 + secondNum *6+thirdNum *36
      
      
   return finalNum
 
      
def decimal_to_ndom (a):
   stra = str(a)
   
   if (len(stra)==1):
      if(a>5):
         numberofsixes= (a-a%6)//6
         remainder = a%6
         finalNum = str(numberofsixes)+str(remainder)
         
         
      else:
         finalNum =a
         
   if (len(stra)==2):
      if(a>35):
         numberofthirtysixes= (a-a%36)//36
         remainder = a%36
         
         numberofsixes= (remainder-remainder%6)//6
         remaindersingle = remainder%6         
         
         finalNum = str(numberofthirtysixes)+str(numberofsixes)+str(remaindersingle)
         
      else:
         numberofsixes= (a-a%6)//6
         remaindersingle = a%6         
                  
         finalNum = str(numberofsixes)+str(remaindersingle)
         

   if (len(stra)==3):
         if(a>35):
            numberofthirtysixes= (a-a%36)//36
            remainder = a%36
            
            numberofsixes= (remainder-remainder%6)//6
            remaindersingle = remainder%6         
            
            finalNum = str(numberofthirtysixes)+str(numberofsixes)+str(remaindersingle)
            
         else:
            numberofsixes= (a-a%6)//6
            remaindersingle = a%6         
                     
            finalNum = str(numberofsixes)+str(remaindersingle)
            
   return finalNum
            
            
            
def ndom_add (a,b):
   valuea = ndom_to_decimal(a)
   valueb = ndom_to_decimal(b)
   
   answer = valuea+valueb
   
   final=decimal_to_ndom (answer)
   return final


def ndom_multiply (a,b):
   valuea = ndom_to_decimal(a)
   valueb = ndom_to_decimal(b)
      
   answer = valuea*valueb
      
   final=decimal_to_ndom (answer)
   return final   
   
   
   
   
   
                  
         
         
         
         
    
         

      
   return finalNum
        
   

                