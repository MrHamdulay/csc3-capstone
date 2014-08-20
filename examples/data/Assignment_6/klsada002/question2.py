"""Adam Kaliski
CSC1015F Assignment 6
question 2
vector operations"""
import math
vector1 = input('Enter vector A:\n')
vector2 = input('Enter vector B:\n')
vectorA = vector1.split()
vectorB = vector2.split()
print('A+B = [',eval(vectorA[0])+eval(vectorB[0]),', ',eval(vectorA[1])+eval(vectorB[1]),', ',eval(vectorA[2])+eval(vectorB[2]),']',sep='')
print('A.B = ',eval(vectorA[0])*eval(vectorB[0])+eval(vectorA[1])*eval(vectorB[1])+eval(vectorA[2])*eval(vectorB[2]),sep='')
print('|A| = %.2f'% (round(math.sqrt(eval(vectorA[0])**2+eval(vectorA[1])**2+eval(vectorA[2])**2),2)),sep='')
print('|B| = %.2f'% (round(math.sqrt(eval(vectorB[0])**2+eval(vectorB[1])**2+eval(vectorB[2])**2),2)),sep='')