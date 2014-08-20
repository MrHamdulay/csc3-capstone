message = input("Enter the message:\n")
rep= eval(input("Enter the message repeat count:\n"))
thick= eval(input("Enter the frame thickness:\n"))
lengt= len(message)

print("+-","-"*(lengt-1),"-"*(thick*2 -1), sep="",end="-+\n")

if thick>1:
      q=0
      for j in range(thick-1):
            print("|"*(q+1),"+","-"*(lengt+(2*thick)-(2*q)-2),"+","|"*(q+1),sep="")
            q=q+1
            
            
for i in range(rep):
      print("|"*thick,message,"|"*thick)
   
if thick>1:
      y=0
      for k in range(thick-1):
            print("|"*(thick-1-y),"+","-"*(lengt+2+(2*y)), "+","|"*(thick-1-y),sep="")
            y=y+1
print("+-","-"*(lengt-1),"-"*(thick*2 -1), sep="",end="-+\n")
