#program to recieve and do calculations with vectors
#victor gueorguiev
#19 april 2014

import math

def get_vector(vectorname):
    sinput = input('Enter vector '+vectorname+':\n')
    vector = sinput.split(' ')
    return vector

def vector_addition(vectorA,vectorB):
    sumvector = []
    for i in range(len(vectorA)):
        sumvector.append(int(vectorA[i])+int(vectorB[i]))
    return ('[{0}, {1}, {2}]').format(sumvector[0],sumvector[1],sumvector[2])

def vector_dotproduct(vectorA,vectorB):
    dotproduct = 0
    for i in range(len(vectorA)):
        dotproduct += int(vectorA[i])*int(vectorB[i])
    return round(dotproduct,2)
        
def vector_mag(vector):
    norm = 0
    for i in range(len(vector)):
        norm += int(vector[i])**2
    norm = math.sqrt(norm)
    return ('{0:.2f}').format(norm)

def main():
    A = get_vector('A')
    B = get_vector('B')
    print('A+B = ',vector_addition(A,B),sep='')
    print('A.B = ',str(vector_dotproduct(A,B)),sep='')
    print('|A| = ',str(vector_mag(A)),sep='')
    print('|B| = ',str(vector_mag(B)),sep='')
main()