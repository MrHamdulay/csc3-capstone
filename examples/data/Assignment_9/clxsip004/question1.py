#Siphesihle Cele
#16 May 2014
#Assignment 9 computer science

#User input requested by program.
#file needs to be read by ther file using the 'r' function for coding.
#empty data list must be created.
#marks should also started at 0
#calculate the mean mark of the data.
#create a loop to obtain the standard deviation.
#also create the formula to calculate the standard deviation.
#calculate students mark, - 1 standard deviation away
#finally a limit of danger should be created for the marks so if they fall in the dangwer zone, the student must see an advisor.

import math


int_input=input("Enter the marks filename:\n") 
def file_data(int_input):
    file_given=open(int_input,"r")  
    data=[]            
    for x in file_given:
        comma=x.split(",")
        data.append(comma)
    file_given.close()
    return data
data=file_data(int_input)


s_marks=0     
for i in data:
    s_marks+=eval(i[1]) 
mean_marks=s_marks/len(data)      

                          
s_numerator=0
for j in data:
    s_numerator+=(eval(j[1])-mean_marks)**2

stand_dev= round(math.sqrt(s_numerator/len(data)),2) 

lower_limit=mean_marks-stand_dev  

students_trouble=[]     
for z in data:
    if eval(z[1])<lower_limit:
        students_trouble.append(z[0])

print("The average is:", "{0:.2f}".format(mean_marks))  
print("The std deviation is:", "{0:.2f}".format(stand_dev))
if students_trouble!=[]:
    print("List of students who need to see an advisor:")
    for s in students_trouble:
        print(s)