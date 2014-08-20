#Python program to analyse student marks read in from a file and determine which students need to see a student advisor.
#Anthony Jacob
#12 May 2014


import math    
marks=[]   
names=[]
names_marks=[]
list_dpr=[]
fname=input("Enter the marks filename:\n")  #asking user for the filename
infile=open(fname,"r")   #opening the actual file

for line in infile:
    items=line.split(",") 
    
    mark= int(items[1].rstrip()) 
    marks.append(mark)
    name=items[0]
    names.append(items[0]) 
    names_marks.append(name)
    names_marks.append(mark) 
    
avg=(sum(marks)/len(marks))
print("The average is:","{0:.2f}".format(avg))
std2=0
for i in marks:
    std1=(avg-i)**2
    std2=std2+std1 
std=math.sqrt(std2/len(marks))   #calculating the standard deviation

print("The std deviation is:","{0:.2f}".format(std))
for position in range(1,len(names_marks)+1,2):
    if names_marks[position]< (avg-std): 
        list_dpr.append(names_marks[position-1]) 
        
if list_dpr:
    print("List of students who need to see an advisor:")  #giving the output
    for a in list_dpr:
        print(a) 
