"""Program to analyse student marks from source file and determine which students
are advised to consult an advisor
thushar hariparsad
11 May 2014"""

file = input("Enter the marks filename:\n")

txtfile = open(file, "r")

list_marks = txtfile.read() #read file into string

txtfile.close()

list_marks = list_marks.split("\n")
list_marks = " ".join(list_marks)
list_marks = list_marks.split(",")
list_marks = " ".join(list_marks)

list_marks = list_marks.split() #read string into a list
marks = []
stds = []
for i in range (0, len(list_marks), 2):
    stds.append(list_marks[i])
    marks.append(eval(list_marks[i+1]))

#calculate the standard deviation      
tot = 0
N = len(marks)
for i in marks:
    tot += i
average = tot/N
sdsum = 0
for i in marks:
    sdsum += (i - average)**2
sd = (sdsum/N)**(1/2)

#append students who are one standard deviation below the mean
new_list = []
for i in range(N):
    if marks[i] < (average - sd):
        new_list.append(stds[i])
        
print("The average is: {0:0.2f}".format(average))
print("The std deviation is: {0:0.2f}".format(sd))
if len(new_list) > 0:
    print("List of students who need to see an advisor:")
for i in new_list:
    print(i)