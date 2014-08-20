"""Question 3- Assignment 8
Duncan Saffy
May 6 2014""" 

def code(x):
   if 1==len(x):
      if x[0]=="z":
         print("a")
      elif 96<ord(x[0])<122:
         order= ord(x[0])+1
         char= chr(order)
         print(char)
      else:
         print(x)
   elif x.isupper():
      print(x)
      
   elif 96<=ord(x[0])<=122:
      if x[0]=="z":
         print("a",end="")
         return code(x[1:])       
     
      else:
         order= ord(x[0])+1
         char= chr(order)
         print(char,end="")      
         return code(x[1:])
   else:
      print(x[0], end="")
      return code(x[1:])
x= input("Enter a message:\n")
print ("Encrypted message:")
code(x)