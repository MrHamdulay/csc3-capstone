''' Program that does basic 3d vector calculation 
Othniel KONAN
KNNOTH001
2014/04/19'''

from math import sqrt

array=[]
A = input('Enter vector A:\n')
B = input('Enter vector B:\n')

#CREATION OF 2D ARRAY OF 3 BY 6
for i in range(6):
    array.append([0]*3)
#SAVE EACH COORDINATES IN THE ARRAY (LINE 1 FOR THOSE OF A, LINE 2-> B)
array[0][0],array[0][1],array[0][2]=map(int,A.split(' '))
array[1][0],array[1][1],array[1][2]=map(int,B.split(' '))

#DEFINE OTHER PART OF THE ARRAY
for i in range(3):
    array[2][i] = array[0][i]+array[1][i]   #Line 2: A+B
    array[3][i] = array[0][i]*array[1][i]   #Line 3: A*B  
    array[4][i] = array[0][i]*array[0][i]   #Line 4: |A|
    array[5][i] = array[1][i]*array[1][i]   #Line 4: |B|

#PRINT THE VALUE
print('A+B =',array[2])
print('A.B =',array[3][0]+array[3][1]+array[3][2])
print('|A| =','{0:3.2f}'.format(sqrt(array[4][0]+array[4][1]+array[4][2])))
print('|B| =','{0:3.2f}'.format(sqrt(array[5][0]+array[5][1]+array[5][2])))