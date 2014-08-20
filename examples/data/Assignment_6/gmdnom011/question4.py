# Program to print a histogram for a list of marks
# Nomsa Gamedze
# 21 April 2014

def get_marks():
    marks = input("Enter a space-separated list of marks:"'\n')
    s_list_marks = marks.split()
    list_marks = []
    for i in s_list_marks:
        mark = eval(i)
        list_marks.append(mark)
    return list_marks

def histogram():
    data = get_marks()
    fail = 0
    third = 0
    lower_second = 0
    upper_second = 0
    first = 0
    for i in data:
        if i < 50:
            fail +=1
        if 50 <= i < 60:
            third += 1
        if 60 <= i <70:
            lower_second +=1
        if 70 <= i < 75:
            upper_second += 1
        if i >= 75:
            first += 1
    print("1 |", "X"*first, sep="")
    print("2+|", "X"*upper_second, sep="")
    print("2-|", "X"*lower_second, sep="")
    print("3 |", "X"*third, sep="")
    print("F |", "X"*fail, sep="")

histogram()