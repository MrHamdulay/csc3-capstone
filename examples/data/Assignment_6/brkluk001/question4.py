'''Program to print a histogram of mark categories
23 April 2014
Luke Barker'''
list_marks = []
from collections import Counter
original_marks = input('Enter a space-separated list of marks:\n').split(' ') #get marks
for i in original_marks:
    x = eval(i)
    if x >= 75:          # checks to see what category each mark is
        list_marks.append('1')
    elif 70 <= x < 75:
        list_marks.append('2+')
    elif 60 <= x < 70:
        list_marks.append('2-')
    elif 50<= x < 60:
        list_marks.append('3')
    else:
        list_marks.append('F')
y = Counter(list_marks)      #counts number of occasions vote appear and adds to a dictionary
ex = 'X'
print('1 |' , ex*y['1'], sep = '')   #prints number of times a category times X to get a histogram
print('2+|' , ex*y['2+'], sep = '')  #prints number of times a category times X to get a histogram
print('2-|' , ex*y['2-'], sep = '')  #prints number of times a category times X to get a histogram
print('3 |' , ex*y['3'], sep = '')   #prints number of times a category times X to get a histogram
print('F |' , ex*y['F'], sep = '')   #prints number of times a category times X to get a histogram


        

    