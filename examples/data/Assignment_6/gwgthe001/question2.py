#Thembekani Gwegwana
# A program to do basic vector calculations in 3 dimensions
# April 2014
def main():
    first_vectors=input('Enter vector A:\n') #Asking user to input vectors A
    A=first_vectors.split()
    second_vectors=input('Enter vector B:\n')#Asking user to input vectors B
    B=second_vectors.split()
    import math #Calculation
    add1=int(A[0])+int(B[0]) #Adding 
    add2=int(A[1])+int(B[1])
    add3=int(A[2])+int(B[2])
    print('A+B = [',add1,',',' ',add2,',',' ',add3,']',sep='')
    mul1=int(A[0])*int(B[0]) #Multiplying
    mul2=int(A[1])*int(B[1])
    mul3=int(A[2])*int(B[2])
    print('A.B =',mul1+mul2+mul3)
    g=math.sqrt(int(A[0])**2+int(A[1])**2+int(A[2])**2)
    print('|A| =','{0:.2f}'.format(g))
    h=math.sqrt(int(B[0])**2+int(B[1])**2+int(B[2])**2)
    print('|B| =','{0:.2f}'.format(h))
main()