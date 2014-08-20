'''marksheet and histogram programme 
Siphesihle Zwane
20/04/14'''
sheet=[]
marks=input('Enter a space-separated list of marks:\n')
a=marks.split(' ') #creating an array for marks
lenght=len(a)

for j in range(lenght): #how many items
    sheet.append(eval(a[j])) #filling in the mark sheet
fail=0 #different catorgories
third=0
lowsec=0
sec=0
first=0
for num in sheet:
    if 0<=num<50:
        fail+=1
    elif 50<=num<60 :
        third+=1
    elif 60<=num<70:
        lowsec+=1
    elif 70<=num<75:
        sec+=1
    elif 75<=num<=100:
        first+=1
print('1 |','X'*first,sep='')
print('2+|','X'*sec,sep='')
print('2-|','X'*lowsec,sep='')
print('3 |','X'*third,sep='')
print('F |','X'*fail,sep='')