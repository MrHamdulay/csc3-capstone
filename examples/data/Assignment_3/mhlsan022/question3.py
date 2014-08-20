'''THIS IS JUST NOT MY WEEK....
THIS ASSIGNMENT IS KICKING MY BEHIND FROM THE FRONT, DON'T ASK ME HOW.'''
#Here goes nothing.
#SandyCris MAHLANGU
#MHLSAN022
def scary(mid):
   for i in range(a):
      print("|"*f,mid,"|"*f)
      #if f>1:
       #  for i in range

def cover():
   i=len(mid)
   x="+"
   y='-'
   z="|"
   q=0
   for j in range(f,0,-1):
      print(z*q+x+y*(i+2*j)+x+z*q)
      q+=1
def dow():
   i=len(mid)
   x="+"
   y='-'
   z="|"
   q=f-1
   for j in range(1,f+1):
      print(z*q+x+y*(i+2*j)+x+z*q)
      q-=1   
      

mid=input('Enter the message:\n')
a=eval(input("Enter the message repeat count:\n"))
f=eval(input('Enter the frame thickness:\n'))
cover()
scary(mid)
dow()