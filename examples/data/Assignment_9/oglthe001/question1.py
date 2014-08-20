"""theresa ogallo 2014
program to analyse student marks read in from a file"""

file=input('Enter the marks filename:\n')

#reading from file
f = open (file, 'r')
lines = f.readlines ()
f.close ()

#getting list of marks
marks=[]            
for j in range (len (lines)):
    lines[j] = lines[j][:]
    new_lines = lines[j].split (',')
    marks.append(eval(new_lines[1]))
    
#calculating average
sum_marks=sum(marks)
average = round(sum_marks/(len(marks)), 2)
print ('The average is:','{0:.2f}'.format(average))

#calculating standard deviation
import math
ans=[]
for i in range (len (marks)):
    ans.append((marks[i]-average)**2)
standard_deviation = round(math.sqrt(sum(ans)/len(ans)), 2)
print('The std deviation is:','{0:.2f}'.format(standard_deviation))

#checking to see if student's mark is less than one standard deviation below the mean
list_answers=[]
for i in marks:
    answer= i-average
    answers_list=list_answers.append(answer)
    if answer < -1 :
        m=marks.index(i)
        name=lines[m][0:]
        list_names=name.split(',')
        final_answer=list_names[0]
        
if 0 in list_answers:
    ''
else:
    print('List of students who need to see an advisor:')
for i in marks:
    answer= i-average
    if answer < -1 :
        m=marks.index(i)
        name=lines[m][0:]
        list_names=name.split(',')
        final_answer=list_names[0]
        print(final_answer)