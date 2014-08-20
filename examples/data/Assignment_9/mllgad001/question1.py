# program to analyse student marks from text file
# mllgad001
# 14 May 2014

import math

# get user to enter filename and open the file
filename = input("Enter the marks filename:\n")        
f = open(filename, "r")

list_ = []
for item in f:    
    line = item.replace('\n', '') # replace new line characters in the file with an empty string
    list_.append(line)      # add names and marks to the main list

marks = []
names = []
for item in list_:    # add names to name list and marks to mark list
    name, mark = item.split(',') # split the names and marks into separate strings
    marks.append(mark) 
    names.append(name)

# calculate the mean
sum_ = 0
for mark in marks:
    mark_int = int(mark)
    sum_ += mark_int
    
mean = round(sum_/len(marks),2)
print("The average is: " + '{0:.2f}'.format(mean))

#calculate the standard deviation
DevSqr = 0
for mark in marks:
    mark_int = int(mark)
    dev = mean - mark_int
    DevSqr += dev**2
    
std_dev = round(math.sqrt(DevSqr/len(marks)),2)
print("The std deviation is: " + '{0:.2f}'.format(std_dev))


diff = mean - std_dev      # calculate the number one std dev away from the mean

st_list = []           # list to store student names 

# determine which students are less than one std dev away from the mean
for mark in marks:
    mark_int = int(mark)
    if mark_int < diff:
        index_mark = marks.index(mark)      # get the index value of the marks
        for name in names:
            index_name = names[index_mark]       # name of the student is in the same index as the low mark
            if name == index_name:
                st_list.append(index_name)         # add the name to the student list

if st_list:
    print("List of students who need to see an advisor:")

for i in st_list:
    print(i)
        
f.close()
