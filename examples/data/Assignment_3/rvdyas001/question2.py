x =eval(input("Enter the height of the triangle:\n"))
def a(width,par2):
     gap=width//2  
     for i in range(0,width,2):
          print(' '*gap,end='')  
          print(par2*(i+1))
          gap=gap-1
          
def sq(H,char):
     for i in range(H):
          print(char*H)  
if __name__ =='__main__':
     a(x*2-1,'*')
     
