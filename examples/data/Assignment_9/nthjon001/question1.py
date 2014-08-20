"""analyse students marks and determine which students need to see a student advisor
Jonathan Nathan
10 may 2014"""

from math import sqrt

# create names list to store names
name_list = []
# creates marks list to store marks
mark_list = []

file_name = input("Enter the marks filename:\n")
f = open(file_name, 'r')

# adds names and marks to lists as 'keys' and 'values', and deletes \n characters
for line in f:
    name_list.append(line[:line.find(',')])
    mark_list.append((line[line.find(',') + 1 : ]).replace('\n',''))
    
f.close()

# create average variable
average = 0

# calculates average
for value in mark_list:
    average += int(value)
average = average / len(mark_list)

# create standard deviation variable
std_dev = 0

# calculates standard deviation
for value in mark_list:
    std_dev += (int(value) - average)**2
std_dev = sqrt(std_dev / len(mark_list))

# creates list to keep all students names who need to see a student advisor
advisor_visit = []

# calculates if a student must see an advisor and appends to advisor_visit list
for name in range(len(name_list)):
    if int(mark_list[name]) < (average - std_dev):
        advisor_visit.append(name_list[name])

# print statements with format strings to 2 decimals of precision
print("The average is:", '{:.2f}'.format(average))
print("The std deviation is:", '{:.2f}'.format(std_dev))
if advisor_visit != []:
    print("List of students who need to see an advisor:")
for name in advisor_visit:
    print(name)