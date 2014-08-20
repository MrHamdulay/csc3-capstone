# tarisai kalinde
# klntar002
# histogram for marks

# taking input
marks= (input('Enter a space-separated list of marks:\n'))
marks_array= marks.split(' ')   # splits string to array

# initialization of accumulation
countfif=0
counthir=0
countlow=0
countup=0
countfir=0
# looping through the list for class evaluation
for i in marks_array:
    
        
    if 0<=int(i)< 50:
        countfif+=1

    if 50<=int(i)<60:
        counthir+=1
    
    if 60<=int(i)<70:
        countlow+=1
    
    if 70<=int(i)<75:
        countup+=1
    
    if 75<=int(i)<=100:
        countfir+=1
    
    
print('1 |','X'*countfir,sep='')
print('2+|','X'*countup,sep='')
print('2-|','X'*countlow,sep='')
print('3 |','X'*counthir,sep='')
print('F |','X'*countfif,sep='')
        
