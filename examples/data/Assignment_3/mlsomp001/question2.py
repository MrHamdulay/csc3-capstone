#prott isosceles
par2=eval(input("Enter the height of the triangle:\n"))
def a(par1,par2):
 gap=par1//2
 for i in range(0,par1+1,2):
  print(" "*(gap),end="")
  print(par2*(i+1))
  gap=gap-1

a(2*par2-1,"*")