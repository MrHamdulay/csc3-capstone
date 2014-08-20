#Romello Naidoo
#NDXROM005
#9 May 2014
def encryption(message,z):
      
 if message=="":
  pass
 else:
  x=ord(message[0])
  
  if 123>x>=97:
   y=x+1
   if y==123:
     z+="a"
     return encryption(message[1:],z)
    
   z+=chr(y)
   return encryption(message[1:],z)
  else:
   z+=chr(x)
   return encryption(message[1:],z)
  
 print("Encrypted message:\n"+z)
 
message=input("Enter a message:\n")
encryption(message,"")
  
  
  