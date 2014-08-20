'''Printing histogram of marks entered as list
Inga Ndyoki
25 April 2014'''

marks = (input('Enter a space-separated list of marks:\n')).split(' ')

first = 0
Usecond =0 
Lsecond = 0
third = 0
fail = 0

for i in range(len(marks)):         #Checking the rating of each mark
    if eval(marks[i]) >= 75:        #Increasing the count of each level found
        first +=1
    elif eval(marks[i]) >= 70:
        Usecond +=1
    elif eval(marks[i]) >= 60:
        Lsecond +=1
    elif eval(marks[i]) >= 50:
        third +=1
    else:
        fail +=1
                                     
                                     #Printing out histogram
print('1 |',('X'*first),sep = '')
print('2+|',('X'*Usecond),sep ='')
print('2-|',('X'*Lsecond),sep ='')
print('3 |',('X'*third),sep = '')
print('F |',('X'*fail),sep = '')