marks = []
x = input('Enter a space-separated list of marks:\n')
marks = x.split()

Fl = 0
Thrd = 0
LwScnd = 0
UpScnd = 0
Frst = 0

count = 0
while count<len(marks):
    if eval(marks[count])<50:
        Fl +=1
    if 50<=eval(marks[count])<60:
        Thrd +=1  
    if 60<=eval(marks[count])<70:
        LwScnd +=1  
    if 70<=eval(marks[count])<75:
        UpScnd +=1 
    if eval(marks[count])>=75:
        Frst +=1  
    count+=1
        
print('1 |'+'X'*Frst)
print('2+|'+'X'*UpScnd)
print('2-|'+'X'*LwScnd)
print('3 |'+'X'*Thrd)
print('F |'+'X'*Fl)
    
