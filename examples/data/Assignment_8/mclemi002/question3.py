"""emile mclennan
6/5/14
A8 Q3"""
def encrypt(x):
   if 96<ord(x[0])<122:
      if x[0]=="z":
         print("a",end="")
         return encrypt(x[1:])       
      elif 1==len(x):
         order= ord(x[0])+1
         char= chr(order)
         print(char,end="")
      else:
         order= ord(x[0])+1
         char= chr(order)
         print(char,end="")      
         return encrypt(x[1:])
   else:
      print(x[0], end="")
      return encrypt(x[1:])
x= input("Enter a message:\n")
print ("Encrypted message:")
encrypt(x)
