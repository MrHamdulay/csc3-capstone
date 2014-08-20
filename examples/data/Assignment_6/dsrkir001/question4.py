#Program that takes in a list of marks and outputs a histogram representation
#20 April 2014
#Kiran Desraj

mark = input('Enter a space-separated list of marks:\n')
mark = ((mark.split()))
mark = list(map(int, mark))


fail = 0
third = 0
lower_second = 0
upper_second = 0
first = 0


for i in mark:
    if i < 50:
        fail = fail + 1
    if 50 <= i < 60:
        third = third +1
    if 60 <= i < 70:
        lower_second = lower_second + 1
    if 70 <= i < 75:
        upper_second = upper_second + 1
    if i >= 75:
        first = first + 1
        
print('1 |','X'*first, sep='')
print('2+|','X'*upper_second, sep='')
print('2-|','X'*lower_second, sep='')
print('3 |','X'*third, sep='')
print('F |','X'*fail, sep='')
    

    
        
    

