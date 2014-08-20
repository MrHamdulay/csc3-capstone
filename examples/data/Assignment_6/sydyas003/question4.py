mark = input("Enter a space-separated list of marks:\n")
marks = mark.split()

count_fail = 0
count_3rd = 0
count_lower2nd = 0
count_upper2nd = 0
count_1st = 0 

for index in range (len(marks)):
    marks[index] = eval(marks[index])
    
for index in marks:
    if(index>=0):
        if(index<50):
            count_fail+=1
        elif(index<60):
            count_3rd+=1
        elif(index<70):
            count_lower2nd+=1
        elif(index<75):
            count_upper2nd+=1
        else:
            count_1st+=1
        
print("1 |","X"*count_1st,sep='')
print("2+|","X"*count_upper2nd,sep='')
print("2-|","X"*count_lower2nd,sep='')
print("3 |","X"*count_3rd,sep='')
print("F |","X"*count_fail,sep='')
        