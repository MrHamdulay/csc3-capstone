#19/03/14
#Shivaan Motilal
#Programme to create a triangle

h=eval(input("Enter the height of the triangle:\n"))
h=h+h
gap=(h)//2
for i in range(1,h,2):
      print(' ' * (gap-1),end='')
      print('*' * (i))
      gap-=1
    

