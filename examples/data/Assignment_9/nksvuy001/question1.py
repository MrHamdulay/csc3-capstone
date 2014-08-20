"""Program to figure out whether students should see student advisor, based on their scores
vuyolwethu nkosi
12 may 2014"""

from math import sqrt #import the square root function 

filename=input("Enter the marks filename:\n") #get the filename from user to work with
infile=open(filename,"r") #open file
lines=infile.readlines() #copy every line of file into variable name "lines"


l=[] #create empty list to store the marks in
students=[] #create list to store the student name and mark
for line in lines:#going through every line
    if(line!=""):
        
        name,mark=line.split(",")[0],line.split(",")[1] #splitting the student names and mark
        if mark[-1]=="\n": #if the mark contains the new line character at the end
            m=mark[:-1] #removing the new line character
            l.append(eval(m)) #adding this mark to the list l
            #for i in range(len(line)):
            students.append([name,eval(mark)]) #adding name and mark to list students
#students[name]=eval(mark[:-1]) 
        else:
            l.append(eval(mark)) #if the mark does not contain the new line character at the end, just add the mark to the list l
            #for i in range(len(line)):
            students.append([name,eval(mark)])#add the student and mark to the list students
#students[name]=eval(mark) 
#print(students)

s=0.0 #initialise sum
count=0 #initialise count
for i in l: #going though list of marks
    s+=i #add the mark to the sum
    count+=1 #add to count
average=s/count #average=sum/count
print("The average is: {0:.2f}". format (average)) #print out

std=0 #initialising standard deviation count
for i in l: #going through list of marks
    std_count=(i-average)**2 #formula
    std+=std_count #add this to the std count
    
standard_deviation=sqrt(std/len(l)) #the actual standard deviation calculation
print("The std deviation is: {0:.2f}".format(standard_deviation)) #print out

"""advise=[] #create list to store students who need to see advisor
for i in range(len(students)):#going through list
    for j in range(i):
        if i[1]<(average-standard_deviation): #if the mark of the student (accessed by it key) is less than one standard deviation below the mean(average)
            advise.append(i[0]) #add to list

if advise!=[]:
    print("List of students who need to see an advisor:")
    for i in advise:
        print(i,sep="") #print out the student names"""

infile.close() #close file

if standard_deviation>0: #if there is a standard_deviation
    print("List of students who need to see an advisor:")
    filey=open(filename,"r") #open file
    for line in filey: #going through lines in file
        name,mark=line.split(",") #splitting lines into name and mark
        fine=average-standard_deviation #the bar 
        if eval(mark)<fine: #if the bar is not met
            print(name) #print that name 
        #else:
            #()
#filey.close()