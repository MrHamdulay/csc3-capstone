def pyramid(A):
    gap=A-1
    B=1
    for i in range(A):
        print(' '*gap,end='')
        print('*'*(i+B))
        gap=gap-1
        B=B+1
if __name__=='__main__':
    A=eval(input('Enter the height of the triangle:\n'))
    pyramid(A)