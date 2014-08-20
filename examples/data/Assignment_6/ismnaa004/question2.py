#25/04/2014
#naadirah Ismail
#does vector calculations in 3 dimensions:addition, dot product and normalization


import math#to use square root
def vector():
    vectorA=input('Enter vector A:\n')
    vectorB=input('Enter vector B:\n')
    #convert input to a list/array; the vector
    listA=vectorA.split(' ')
    listB=vectorB.split(' ')
    #assigns the values to the indices of the list
    x1=listA[0]
    x2=listA[1]
    x3=listA[2]
    y1=listB[0]
    y2=listB[1]
    y3=listB[2]
    #calculates addition,dot production and normalization
    sum=[int(x1)+int(y1),int(x2)+int(y2),int(x3)+int(y3)]
    times=int(x1)*int(y1)+int(x2)*int(y2)+int(x3)*int(y3)
    absA=math.sqrt((int(x1)**2)+(int(x2)**2)+(int(x3)**2))
    absB=math.sqrt((int(y1)**2)+(int(y2)**2)+(int(y3)**2))
    print('A+B =',sum)
    print('A.B =',times)
    print('|A| =','%0.2f'%(absA))#uses formatting to output ans
    print('|B| =','%0.2f'%(absB))

vector()