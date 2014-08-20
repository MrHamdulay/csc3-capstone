#-------------------------------------------------------------------------------
# Name:        question4
# Purpose:     a program that takes in a list of marks (separated by spaces)
#              and outputs a histogram representation of the marks according to
#               the mark categories at UCT
#
# Author:      Lungelo
#
# Created:     21/04/2014
# Copyright:   (c) Lungelo 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#get user to input data
marks=input("Enter a space-separated list of marks:\n")

marks=marks.split(' ')

dictionary={'1':0,'2+':0,'2-':0,'3':0,'F':0}
for i in range(len(marks)):
    marks[i]=eval(marks[i])

for i in marks:
    if i>=75:
        dictionary['1']+=1
    elif 70<=i<=75:
        dictionary['2+']+=1
    elif 60<=i<=70:
        dictionary['2-']+=1
    elif 50<=i<=60:
        dictionary['3']+=1
    else:
        dictionary['F']+=1

print('{0:<2}'.format('1'),'|','X'*dictionary['1'],sep='')
print('{0:<2}'.format('2+'),'|','X'*dictionary['2+'],sep='')
print('{0:<2}'.format('2-'),'|','X'*dictionary['2-'],sep='')
print('{0:<2}'.format('3'),'|','X'*dictionary['3'],sep='')
print('{0:<2}'.format('F'),'|','X'*dictionary['F'],sep='')


