'''program to analyse student marks read in from a file and determine which students need to see a student advisor
Patrick Boroughs
10 May 2014'''

#get filename
filename = input("Enter the marks filename:\n")

#open file and read lines to array
f = open(filename,'r')
lines = f.readlines()

#remove extra \n
for i in range(len(lines)):
    if lines[i][-1:]=='\n':
        lines[i]=lines[i][:-1]

#create array of just marks, and sum marks for total
marks=[]
total=0
for i in range(len(lines)):
    pos = lines[i].index(',')
    mark=eval(lines[i][pos+1:])
    marks.append(mark)
    total+=mark
 
#average calculation   
average=total/len(lines)

#standard deviation calculation
variance=0
for mark in marks:
    variance+=((mark-average)**2)
    
stddev=(variance/len(lines))**(1/2)

#output
print("The average is:","{0:.2f}".format(average))
print("The std deviation is:","{0:.2f}".format(stddev))

for i in range (len(marks)):
    if marks[i]<(average-stddev):
        print("List of students who need to see an advisor:")
        break

#test if student is below mean minus 1 std dev
for i in range (len(marks)):
    if marks[i]<(average-stddev):
        pos = lines[i].index(',')
        print(lines[i][:pos])
        
#close file
f.close()