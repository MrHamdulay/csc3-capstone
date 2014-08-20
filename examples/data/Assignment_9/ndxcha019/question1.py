'''program to determine which students must see an adviser, using standard deviation from an average
Luke Naude
11 May 2014'''

#get input for filename
file_name=input('Enter the marks filename:\n')

#open file and add info to a list
file=open(file_name,"r")
lines=file.readlines()
file.close()

# chop off the trailing carriage returns
for i in range (len (lines)):
    lines[i] = lines[i][:-1]

#split student name from grade
new_lines=[]
for line in lines:
    new_lines.append(line.split(','))
    

#pull corresponding marks and name and add to lists
marks=[]
names=[]
for i in new_lines:
    for j in i:
        if eval(i[1]) not in marks:
            marks.append(eval(i[1]))
        if i[0] not in names:
            names.append(i[0])  
      
    
average=0

#function to calculate average
def make_average():
    global average
    mark_total=0
    entry_count=0
    for i in marks:
        mark_total+=i
        entry_count+=1
    average=mark_total/entry_count
make_average()          
    
#function to calculate standard deviation
import math #so that sqrt and exponents can be used
n=0
dev=0
def std_dev(n):
    global dev
    if n==len(marks):
        return math.sqrt(dev/len(marks))
    if n<len(marks):
        dev+=(marks[n]-average)**2
        return std_dev(n+1)
    
std_deviation=std_dev(n)

#print average
print('The average is: {:.2f}'.format(average))

#print standard deviation
print('The std deviation is: {:.2f}'.format(std_deviation))

#list of students who's marks are one std dev below average
x=0
def thick_list(x):
    if x<len(marks):
        if marks[x]>(average-std_deviation):#skip students with good grades
            return thick_list(x+1)
        if (average-std_deviation)>=marks[x]:#print the names of students with bad grades
            print(names[x])
            return thick_list(x+1)
    else:
        return False

#if student marks <= average - standard deviation, print their names
print('List of students who need to see an advisor:')
thick_list(x)