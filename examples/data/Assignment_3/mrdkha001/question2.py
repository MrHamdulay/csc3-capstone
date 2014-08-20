          
def a(height,sym):
 gap=height -1
 for i in range(0,height+height,2):
  print(' '*gap,end='') 
  print(sym*(i+1))
  gap=gap-1
  
height = eval(input("Enter the height of the triangle:\n"))
a(height, "*")
              