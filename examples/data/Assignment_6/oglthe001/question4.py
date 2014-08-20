"""theresa ogallo 2014
histogram representation of marks"""

#getting the marks
marks = [int(i) for i in (input('Enter a space-separated list of marks:\n')).split()]
new_marks=[]
for i in marks:
    if i < 50:
        i='fail'
        new_marks.append(i)
    elif 50 <= i < 60:
        i='third'
        new_marks.append(i)
    elif 60 <= i < 70:
        i='lower_second'
        new_marks.append(i)
    elif 70 <= i < 75:
        i='upper_second'
        new_marks.append(i)
    elif i >= 75:
        i='first'
        new_marks.append(i)
marks = new_marks

#counting the number of marks that satisfy the conditions of each category
marks.count('fail')
marks.count('third')
marks.count('lower_second')
marks.count('upper_second')
marks.count('first')

print('1 |'+'X'*marks.count('first'))
print('2+|'+'X'*marks.count('upper_second'))
print('2-|'+'X'*marks.count('lower_second'))
print('3 |'+'X'*marks.count('third'))
print('F |'+'X'*marks.count('fail'))