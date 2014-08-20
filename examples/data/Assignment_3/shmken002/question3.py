#Using if, for and while loops to make shapes
#Kenneth Shimabukuro
#19/03/14


word=input("Enter the message:\n")
mrc= eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
          
def frame():
   x=(2*thickness+len(word)+2)
   y=(len(word))
   for i in range(0, thickness, 1):
      x-=2
      print("|"*(i) + "+" + "-"*(x) + "+" + "|"*(i))
         #print("|", sep="|"*(thickness+mrc))
   for j in range(0,mrc,1):
      print("|"*(thickness)+ " " + word + " " + "|"*(thickness))
   for k in range(thickness-1, -1, -1):
      y+=2
      print("|"*(k) + "+" + "-"*(y) + "+" + "|"*(k))
frame()       



#mrc= int(input("Enter the message repeat count:\n"))
#thickness= int(input("Enter the frame thickness:\n"))
#def frame():
 #  for i in range(0,mrc+thickness,1):
  #    print("|"*(thickness))
#frame()      