#Zikho Godana
#25 March 2014
#program to draw an isoceles triangle of a given height using the '*' character.

height=eval(input("Enter the height of the triangle:\n"))

def tri(height):
     gap=height-1  
     for i in range(0,height):
          print(' '*gap,end='')
          if i==0:
               print('*'*(i+1))
          else:
               print('*'*(i*2+1))
          gap=gap-1 # can also write this as: gap-=1  
        
tri(height)
            

