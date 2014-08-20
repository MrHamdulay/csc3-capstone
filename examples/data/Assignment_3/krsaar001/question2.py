def tri():
     x = eval(input("Enter the height of the triangle:\n"))
     stars = 2*x
     gap= x - 1
     for i in range(0,stars,2):
          print(' ' * gap,end = '')
          print('*' * (i + 1))
          gap = gap - 1 
tri()