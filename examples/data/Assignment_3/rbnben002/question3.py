x = input("Enter the message:\n")
y= eval(input("Enter the message repeat count:\n"))
thickness= eval(input("Enter the frame thickness:\n"))
length= len(x)
print("+-","-"*(length-1),"-"*(thickness*2 -1), sep="",end="-+\n")
if thickness>1:
      q=0
      for j in range(thickness-1):
            print("|"*(q+1),"+","-"*(length+(2*thickness)-(2*q)-2),"+","|"*(q+1),sep="")
            q=q+1
for i in range(y):
      print("|"*thickness,x,"|"*thickness)
if thickness>1:
      y=0
      for k in range(thickness-1):
            print("|"*(thickness-1-y),"+","-"*(length+2+(2*y)), "+","|"*(thickness-1-y),sep="")
            y=y+1
print("+-","-"*(length-1),"-"*(thickness*2 -1), sep="",end="-+\n")