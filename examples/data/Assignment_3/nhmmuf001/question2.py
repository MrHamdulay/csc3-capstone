# question2.py
# Mufudzi Nhamoinesu
# Program to print an isoceles triangle 
def a(par1,par2):
 gap=par1//2 
 for i in range(0,par1,2):
  print(' '*gap,end='')
  print(par2*(i+1))
  gap=gap-1 
def sq(H,char):
 for i in range(H):
  print(char*H) 
if __name__ =='__main__':
  m=eval(input("Enter the height of the triangle:\n"))
  a(m*2,'*')
