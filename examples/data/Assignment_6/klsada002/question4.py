"""Adam Kaliski KLSADA002
CSC1015F Assignment 6 Question 4
representing mark distribution on a bar graph"""
s = input('Enter a space-separated list of marks:\n')
marks = s.split(' ')
first=0
twoplus=0
twominus=0
three=0
fail=0
marks = marks
for i in marks:
    if eval(i) < 50:
        fail+=1
    elif eval(i) >= 50 and eval(i) < 60:
        three+=1
    elif eval(i) >= 60 and eval(i) < 70:
        twominus +=1
    elif eval(i) >= 70 and eval(i) < 75:
        twoplus+=1
    elif eval(i) >= 75:
        first+=1
print('1 |','X'*first,sep='')
print('2+|','X'*twoplus,sep='')
print('2-|','X'*twominus,sep='')
print('3 |','X'*three,sep='')
print('F |','X'*fail,sep='')
        
        