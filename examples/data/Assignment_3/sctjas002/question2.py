height=eval(input("Enter the  height of the triangle:\n"))   
def a(width,height):
     gap=width//2 
     for i in range(0,width,2):
          print(' '*gap,end='')  
          print(height*(i+1))
          gap=gap-1

def sq(h,char):
     for i in range(height):
          print(char*height)         
if __name__ =='__main__':
     a(height + height,'*')

 
 
