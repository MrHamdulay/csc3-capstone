"""Dumisani Ngwenza
NGWDUM005
23/04/2014
Assignment 6 Question 4"""

#create an empty array 
mark_list = []

#get inputs
marks = input("Enter a space-separated list of marks:\n")

#populate array
mark_list = marks.split(' ')

fail = 0
third = 0
lower_2nd = 0
upper_2nd = 0
first = 0

#iterate through list
for number in mark_list:
    mark = eval (number)
    if mark<50:
        fail += 1
    if 50 <= mark < 60:
        third += 1
    if 60 <= mark < 70:
        lower_2nd += 1
    if 70 <= mark < 75:
        upper_2nd += 1
    if mark >=75:
        first += 1

#create histogram
print ('1 |', 'X'*first, sep='')
print ('2+|', 'X'*upper_2nd, sep='')
print ('2-|', 'X'*lower_2nd, sep='')
print ('3 |', 'X'*third, sep='')
print ('F |', 'X'*fail, sep='')

#print (mark_list)
