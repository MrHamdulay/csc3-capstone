""" Analyse student marks read in from a file and determine which students need to see a student advisor
Elizabeth Cilliers
11/05/2014"""

filename=input("Enter the marks filename:\n")
f=open(filename,"r")
lines=f.readlines() #returns a list of the lines in the file. Each list item is a single line including the newline character at the end. Each line contains student number and mark separated by a coma.
f.close()

#create list of names
listofnames=[]
for i in range (len(lines)):
                if lines[i][-4]==",":
                                name=lines[i][0:-4]
                                listofnames.append(name)
                else:
                                name=lines[i][0:-3]
                                listofnames.append(name)                                

#create list of marks
listofmarks=[]
for i in range (len(lines)):
                if lines[i][-3]!=",": 
                                mark=lines[i][-3:-1] #for double digit numbers
                                mark=eval(mark)
                                listofmarks.append(mark)
                else:                
                                mark=lines[i][-2] #for single digit marks
                                mark=eval(mark)
                                listofmarks.append(mark)
                                                                    
#calculating average
marksum=0
for i in range (len(listofmarks)):
                mark=listofmarks[i]
                marksum+=mark

average=marksum/(len(listofmarks)) #average is sum of marks divided by number of students/lines.
ave='{0:0.2f}'.format(average)
print("The average is:",ave)

#calculating standard deviation
devsum=0
for i in range (len(listofmarks)):
                mark=listofmarks[i]                
                x=(mark-average)**2
                devsum+= x

stdDev=(devsum/(len(listofmarks)))**0.5
SDev='{0:0.2f}'.format(stdDev)
print("The std deviation is:",SDev)

#list of students who need to see an advisor
students=[]
for i in range(len(listofnames)):
                if listofmarks[i]<(average-stdDev):
                                students.append(listofnames[i])
if students:
                print("List of students who need to see an advisor:")
                for i in range (len(students)):
                                print(students[i])