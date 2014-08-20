import math
"""get input from the user"""
filename=input("Enter the marks filename:\n")
f=open(filename, "r") 
lines=f.readlines() #to read the lines of file
f.close()


names_list=[]
marks_list=[]
for name in lines:
    name_list=name.split(",")
    for item in name_list:
        item=item.replace("\n","")
        if item.isdigit():
            marks_list.append(item)
        else:
            names_list.append(item)

counter=0        
for mark in  marks_list:
    counter+=int(mark)
   
average=((counter)/(len(marks_list)))

#to calculate the standard deviation

square_sum = 0
for name in range (len(lines)):
        names=lines[name]
        names2=names.split(',')
        marks=int((names2[-1]))
        square=(marks-average)**2
        square_sum+=square

stndrd_dev=math.sqrt((square_sum)/(len(marks_list)))

print("The average is: {:.2f}".format(average))

print("The std deviation is: {:.2f}".format(stndrd_dev))

#to get list of students who need to see student advisor
names_list=''
for name in range (len(lines)):
        names=lines[name]
        names2=names.split(',')
        if (int(names2[-1])) < (average-stndrd_dev):
                names_list+=(names2[0]) + '\n'
if stndrd_dev>0:
    print("List of students who need to see an advisor:")
    print(names_list)    
