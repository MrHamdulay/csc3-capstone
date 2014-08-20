'''Program that outputs a histogram representation of the marks
21 April 2014
Matshepo Malatji'''

#Receive marks from user and place in list
marks = input("Enter a space-separated list of marks:\n").split(' ')
#print(marks)

#Determine the number of marks that fall within each category
fail = 0
third = 0
lower_second = 0
upper_second = 0
first = 0

for i in marks:
    if int(i) < 50:
        fail += 1
    elif (int(i) >= 50) and (int(i)< 60):
        third += 1
    elif (int(i) >= 60) and (int(i) <70):
        lower_second += 1
    elif (int(i) >= 70) and (int(i) < 75):
        upper_second += 1
    else:
        first += 1

#Display histogram
print('1 |' + 'X'*first)
print('2+|' + 'X'*upper_second)
print('2-|' + 'X'*lower_second)
print('3 |' + 'X'*third)
print('F |' + 'X'*fail)