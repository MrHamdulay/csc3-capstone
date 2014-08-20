'''functions to find the dot product of 2 vectors
tom new
2014/04/12'''
import math

def getvect (vector_name):
    '''asks user for a vector and converts it to list format'''
    print ('Enter ', vector_name, ':', sep = '')
    vector = input ()
    vector = vector.split (' ')
    vector = [eval (i) for i in vector]
    return vector

def addvect (a, b):
    '''adds two vectors in list form'''
    vector = [i + j for i, j in zip (a, b)]
    return vector

def dotvect (a, b):
    '''finds the dot product of two vectors in list form'''
    vector = [i * j for i, j in zip (a, b)]
    return sum (vector)

def normvect (vector):
    '''normalizes a vector in list form, returns to 2 decimal places'''
    vectorsq = [i**2 for i in vector]
    x = math.sqrt (sum (vectorsq))
    return round (x * 100) / 100

if __name__ == '__main__':
    a = getvect ('vector A')
    b = getvect ('vector B')
    print ('A+B =', addvect (a, b))
    print ('A.B =', dotvect (a, b))
    print ('|A| =', '%0.002f' %(normvect (a)))
    print ('|B| =', '%0.002f' %(normvect (b)))