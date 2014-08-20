"""
"""
def grades():
    marks=input('Enter a space-separated list of marks:\n')
    marks=marks.split()
    marks = list(map(int, marks))
    first = []
    second = []
    third = []
    fourth = []
    fail = []
    for i in range(len(marks)):
        if marks[i]>=75:
            first.append(marks[i])  
        if 70 <= marks[i] < 75:
            second.append(marks[i])
        if 60 <= marks[i] < 70:
            third.append(marks[i])
        if 50 <= marks[i] < 60:
            fourth.append(marks[i])
        if marks[i] < 50:
            fail.append(marks[i])
    print("1 |"+"X"*len(first))
    print("2+|"+"X"*len(second))
    print("2-|"+"X"*len(third))
    print("3 |"+"X"*len(fourth))
    print("F |"+"X"*len(fail))
grades()
    