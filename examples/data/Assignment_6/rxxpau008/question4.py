#Description: Creates a simple histogram based on marks entered
#Name: Paul Roux - RXXPAU008
#Date: 22 April 2014

entry = input("Enter a space-separated list of marks:\n")
marks = entry.split()

first = 0
upper_second = 0
lower_second = 0
third = 0
fail = 0

for i in marks:#Sorts the marks into the specified categories
    i = eval(i)
    if i >=75:
        first+=1
    elif i < 75 and i >= 70:
        upper_second+=1
    elif i < 70 and i >= 60:
        lower_second+=1
    elif i < 60 and i >= 50:
        third+=1
    elif i < 50:
        fail+=1
#Prints the Histogram        
print('1 |','X'*first,sep='')
print('2+|','X'*upper_second,sep='')
print('2-|','X'*lower_second,sep='')
print('3 |','X'*third,sep='')
print('F |','X'*fail,sep='')