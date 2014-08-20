#Romello Naidoo
#NDXROM005
#9 May 2014
def pairs(string,count):

 if len(string)==0 or len(string)==1 or string=="":
  pass 
 elif string[0]==string[1]:
  count+=1
  return pairs(string[2:],count)
 else:
  return pairs(string[2:],count)
 
 print("Number of pairs:" ,count) 

   
string=input("Enter a message:\n")
pairs(string,0)
