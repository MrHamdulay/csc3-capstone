''' Program that outputs a histogram representation of the marks according to the mark categories at UCT
Author:Raees Eland
Date:20 April 2014'''

list_of_marks=input('Enter a space-separated list of marks:\n')
list_of_marks=list_of_marks.split(' ')

# takes the list of marks given and determines how many of those marks lies within each interval
first_tally=0
upper_second_tally=0
lower_second_tally=0
third_tally=0
fail_tally=0
for i in list_of_marks:
    if 100>=eval(i)>=75:
        first_tally+=1
    elif 70<=eval(i)<75:
        upper_second_tally+=1
    elif 60<=eval(i)<70:
        lower_second_tally+=1
    elif 50<=eval(i)<60:
        third_tally+=1
    else:
        fail_tally+=1
        
# Prints histogram        
print('1 |','X'*first_tally,sep='')
print('2+|','X'*upper_second_tally,sep='')
print('2-|','X'*lower_second_tally,sep='')
print('3 |','X'*third_tally,sep='')
print('F |','X'*fail_tally,sep='')


    
