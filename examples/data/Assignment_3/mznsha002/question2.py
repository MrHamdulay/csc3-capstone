#Drawing an isoceles triangle using "*"
#21 March 2014

height = eval(input("Enter the height of the triangle:\n"))

def tri():
     gap=height
     for i in range(0,(height*2),2):
          print(' '*(gap-1),end='') 
          print('*'*(i+1))
          gap=gap-1
       
tri()

