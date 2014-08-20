#Mufaro Chiwara - April 2014
#Get list of marks
marks = input('Enter a space-separated list of marks:\n').split(" ")
a,b,c,d,f = 0,0,0,0,0
table = {}
for i in range (len(marks)):
    marks[i]=eval(marks[i])

#Categorise marks
for mark in marks:
    
    if mark >=75:
        a+=1
    elif mark>=70:
        b+=1
    elif mark>=60:
        c+=1
    elif mark>=50:
        d+=1
    else:
        f+=1

#Print function
print('1 |', 'X'*a,sep='')
print('2+|', 'X'*b,sep='')
print('2-|', 'X'*c,sep='')
print('3 |', 'X'*d,sep='')
print('F |', 'X'*f,sep='')
    
    

        
        