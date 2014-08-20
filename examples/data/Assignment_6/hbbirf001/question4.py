# Histogram
# Irfan Habib
# 2014/04/24

def main():
    s = input('Enter a space-separated list of marks:\n')
    marks = s.split(' ')
    fail = 0
    third = 0
    lower2 = 0
    upper2 = 0
    first = 0
    for k in range(len(marks)):
        mark = int(marks[k])
        if mark < 50:
            fail += 1
        elif mark < 60:
            third += 1
        elif mark < 70:
            lower2 += 1
        elif mark < 75:
            upper2 += 1
        elif mark <= 100:
            first += 1
        else: print('Please enter a legitimate result')
        
    print('1 |' + first*'X')
    print('2+|' + upper2*'X')
    print('2-|' + lower2*'X')
    print('3 |' + third*'X')
    print('F |' + fail*'X')
    
main()
        
