 #question3.py
 # Mufudzi Nhamoinesu
 # program to print frame around message.
def main():
   m = input("Enter the message:\n")
          
   r = eval(input("Enter the message repeat count:\n"))
 
   t = eval(input("Enter the frame thickness:\n"))  

   FIXED_LENGTH = len("|| "+m+" ||")
 
   if  r >=1:
      for x in range(0,t-1):
         print("|"*x, "+" , "-" * ((len(m))+((t-x)*2)),"+","|"*x,sep="")
   
   print("|"*(t-1),"+","-"*(FIXED_LENGTH-4),"+", "|"*(t-1),sep="")
  
   for y in range(r):
      print("|"*t," ", m, " ","|"*t,sep="")
      
   for z in range(t-1,-1,-1):
      print("|"*z,"+","-"*((len(m))+((t-z)*2)),"+","|"*z,sep="")
main()
