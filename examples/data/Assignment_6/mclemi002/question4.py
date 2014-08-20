#emile mclennan
#A6
#Q4

StrMarks=[]
StrMarks = input('Enter a space-separated list of marks:\n').split(' ')
marks=[]
for i2 in range(len(StrMarks)): #convert marks to int
    rand = eval(StrMarks[i2])
    marks.append(rand)

count1 =0
count2=0
count3=0
count4=0
count5=0
num = len(marks)

for i in range(num):
    if marks[i] < 50:
        count1+=1
    elif marks[i] >=50 and marks[i] <60:
        count2+=1
    elif marks[i] >=60 and marks[i]<70:
        count3+=1
    elif marks[i] >=70 and marks[i] <75:
        count4+=1
    else:
        count5+=1

         
print('1 |'+str(count5*'X'))
print('2+|'+str(count4*'X'))
print('2-|'+str(count3*'X'))
print('3 |'+str(count2*'X'))
print('F |'+str(count1*'X'))
        