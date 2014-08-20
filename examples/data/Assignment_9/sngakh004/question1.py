"""
Akhil Singh
SNGAKH004
11 May 2014"""

f = input("Enter the marks filename:\n") #Get name of file from user

textfile = open(f, "r")     #Open file

mark_list = textfile.read() #Read the file into a string

textfile.close()

mark_list = mark_list.split("\n")
mark_list = " ".join(mark_list)
mark_list = mark_list.split(",")
mark_list = " ".join(mark_list)

                
mark_list = mark_list.split()  #Read string into a list.
mark = []
student = []
for ml in range (0, len(mark_list), 2):
    student.append(mark_list[ml])
    mark.append(eval(mark_list[ml+1]))

                                        #Calculates the standard deviation of the marks .    
totl = 0
M = len(mark)
for m in mark:
    totl += m
average = totl/M
standard_deviation_sum = 0
for m in mark:
    standard_deviation_sum += (m - average)**2
standard_deviation = (standard_deviation_sum/M)**(1/2)

#Finds the students who are below the std devaition of the mean and adds them to a list.
faillist = []
for m in range(M):
    if mark[m] < (average - standard_deviation):
        faillist.append(student[m])
        

print("The average is: {0:0.2f}".format(average))
print("The std deviation is: {0:0.2f}".format(standard_deviation))
if len(faillist) > 0:
    print("List of students who need to see an advisor:")
for f in faillist:
    print(f)