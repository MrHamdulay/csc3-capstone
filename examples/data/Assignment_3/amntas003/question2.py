x=eval(input("Enter the height of the triangle: \n"))
y="*"
def a():
 if x==0:
  print(" ")
 
 if x>0:
  gap=x//x+(x-2)
 for i in range(0, x, 1):
   print(' '*gap,end='')
   print(y*(i*2+1))
   gap=gap-1

  
def sq(H,char):
 for i in range(H):
  print(char*H)
  
a()