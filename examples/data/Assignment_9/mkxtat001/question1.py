"""MKXTAT001 Tato Moaki
Program analyses student marks read in from a file and determines which students to see advisor
Assignment9 quesion1
2014/05/13"""

import math #import the math library 

filename = input("Enter the marks filename:\n")

infile = open(filename,"r")
lines = infile.readlines()#create a list of strings from content read in file
infile.close()

marks_dictionary = {} #create a dictionary to store student names with marks
#create lists for different manipulations
average_list = []
deviation_list = []
advisor_list = []

#add the name of student to the dictionary with their mark respectively
for line in lines:
    line = line.split(",")
    marks_dictionary[line[0]] = int(line[1])

#collect student marks into one list
for values in marks_dictionary.values():
    average_list.append(values)

average = sum(average_list) / len(average_list)# calculate average

#collect student marks into a list the difference of each mark to the average then square the value
for a_value in marks_dictionary.values():
    difference = a_value - average
    deviation_list.append(math.pow(difference,2))
    
function = (sum(deviation_list))/ len(deviation_list)

standard_deviation = math.sqrt(function)#calculate deviation

print("The average is: {0:0.2f}".format(average))
print("The std deviation is: {0:0.2f}".format(standard_deviation))

#open the file again to obtain the order of student to see advisor
student_file = open(filename, "r")
file_line = student_file.readlines()
student_file.close()

for student in file_line:
    student = student.split(",")
    name = student[0]
    mark = eval(student[1])#evaluate to the underlying data type
    if mark < (average - standard_deviation):
        advisor_list.append(name)
        
#print student advisor list only if there are people in it
if len(advisor_list) > 0:
    print("List of students who need to see an advisor:")
    for person in advisor_list:
        print(person)
    

    


