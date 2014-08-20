'''Mark categorising program
Frans Ledwaba
24 April 2014'''

#collect the marks into a list
marks = input('Enter a space-separated list of marks:\n')
mark = marks.split( )

#evalute the marks
for i in range(len(mark)):
    mark[i] = eval(mark[i])
    
#create variables and sort the marks
a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(len(mark)):
    if 75 <= mark[i] <= 100:
        a += 1
    elif 70 <= mark[i] < 75:
        b += 1
    elif 60 <= mark[i] < 70:
        c += 1
    elif 50 <= mark[i] < 60:
        d += 1
    elif 0 <= mark[i] < 50:
        e += 1
        
#print the marks
print('1 |', 'X' * a, sep='')
print('2+|', 'X' * b, sep='')
print('2-|', 'X' * c, sep='')
print('3 |', 'X' * d, sep='')
print('F |', 'X' * e, sep='')