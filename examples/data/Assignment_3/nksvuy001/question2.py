#program to draw an isosceles triangle
#vuyolwethu nkosi
#24 march 2014

def isoceles():
     height=eval(input("Enter the height of the triangle:\n"))
     star="*"
     space=height-1
     for i in range(0,height+height-1,2):
          print(" "*space,end="")  
          print(star*(i+1))
          space=space-1 
        
isoceles()