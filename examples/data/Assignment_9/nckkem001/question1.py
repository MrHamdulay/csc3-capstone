"""Program to analyse student marks from source file and determine which students
are advised to consult an advisor.
Kemeshan Naicker
11 May 2014"""


#Prompt user for name of source file.
file = input("Enter the marks filename:\n")

#Open file for processing
txtfile = open(file, "r")

#Read file into a string, and replace newline characters with spaces in order to
#read string into a list.
markslist = txtfile.read()

txtfile.close()


markslist = markslist.split("\n")
markslist = " ".join(markslist)
markslist = markslist.split(",")
markslist = " ".join(markslist)
#Read string into a list.
markslist = markslist.split()
marks = []
students = []
for i in range (0, len(markslist), 2):
    students.append(markslist[i])
    marks.append(eval(markslist[i+1]))
    
#Calculate standard deviation.    
total = 0
N = len(marks)
for i in marks:
    total += i
avrg = total/N
sdsum = 0
for i in marks:
    sdsum += (i - avrg)**2
sd = (sdsum/N)**(1/2)

#Find students who are below one standard deviation of the mean and append them
#to a new list.
fail_list = []
for i in range(N):
    if marks[i] < (avrg - sd):
        fail_list.append(students[i])
        
#Print output.
print("The average is: {0:0.2f}".format(avrg))
print("The std deviation is: {0:0.2f}".format(sd))
if len(fail_list) > 0:
    print("List of students who need to see an advisor:")
for i in fail_list:
    print(i)