#Thembekani Gwegwana
#GWGTHE001
#A program to draw an isoceles triangle of a given height using the * character.
 
def tri():
  height=eval(input('Enter the height of the triangle:\n'))
  num=1
  gap=height-1
  for i in range(0,height) :
    print(' '*gap,end='')
    print('*'*num)
    num+=2  
    gap=gap-1
tri()