#starsoceles

h=eval(input("Enter the height of the triangle:\n"))

def starsoceles():
     gap=h
     for i in range(0,(h*2),2):
          print(' '*(gap-1),end='') 
          print('*'*(i+1))
          gap=gap-1
       
starsoceles()