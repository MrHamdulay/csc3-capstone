marks=input('Enter a space-separated list of marks:\n')
marks_list=marks.split(' ')
marks_list = [int(i) for i in marks_list]
fail=0
third=0
low_second=0
up_second=0
first=0
for i in marks_list:
    if i<50:
        fail+=1
    elif i<60:
        third+=1
    elif i<70:
        low_second+=1
    elif i<75:
        up_second+=1
    elif i>=75:
        first+=1
print('1 |','X'*first,sep='')
print('2+|','X'*up_second,sep='')
print('2-|','X'*low_second,sep='')
print('3 |','X'*third,sep='')
print('F |','X'*fail,sep='')
        