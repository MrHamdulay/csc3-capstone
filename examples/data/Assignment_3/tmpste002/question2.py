__author__ = 'TMPSTE002 - Stephen Temple'

def printTriangle(h):
    count_asterix = 1
    count_space = h - 1
    for i in range(h):
        print(' '*count_space, end='')
        print('*'*count_asterix)
        count_asterix += 2
        count_space -= 1

if __name__ == '__main__':
    h = eval(input("Enter the height of the triangle:\n"))
    printTriangle(h)