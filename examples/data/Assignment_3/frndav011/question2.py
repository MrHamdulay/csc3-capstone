def a(width,par2):
     space=width//2 
     for i in range(0,width,2):
          print(' '*space,end='')  
          print(par2*(i+1))
          space=space-1 

n=eval(input("Enter the height of the triangle:\n"))
a(n+4,'*')

