# program to display histogram of marks
# by Jacob Mwanza
# 23/04/2014

def mark():
    fail = ''
    third = ''
    lower2nd = ''
    upper2nd = ''
    first = ''
    marks = []
    # enter the marks
    enter_marks = input("Enter a space-separated list of marks:\n")
    marks = enter_marks.split(' ')
    
    # classify marks
    for i in range(len(marks)):
        mark = int(marks[i])
        if mark < 50:
            fail += 'X'
        elif 50 <= mark < 60:
            third += 'X'
        elif 60 <= mark < 70:
            lower2nd += 'X'
        elif 70 <= mark < 75:
            upper2nd += 'X'
        elif mark >= 75:
            first += 'X'
    
    # print histogram
    print('1 |',first,sep='')
    print('2+|',upper2nd,sep='')
    print('2-|',lower2nd,sep='')
    print('3 |',third,sep='')
    print('F |',fail,sep='')
    
       
mark()
    