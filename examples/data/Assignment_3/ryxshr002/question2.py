#module mystery.py
def a():
     
     height=eval(input("Enter the height of the triangle: \n"))
     
     gap=(height-1) 
     i=1
     for j in range(0,height):
          print(' '*gap,end='')  
          print("*"*(i))
          gap=gap-1
          i=i+2
a()
     