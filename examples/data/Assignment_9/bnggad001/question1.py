""" A Python program to analyse student marks read in from a file and determine which students need to see a student advisor """
""" Gadziraiushe Bangure """
""" 16 May , 2014 """


import math   #import the math library

fname = input('Enter the marks filename:\n')  
f = open(fname,'r')
marks_list1=f.readlines()  #read all the lines into a list  
f.close()

# initialize variables 
k=0      
total_marks=0  
marks=[]  
marks_list2=[]   


for i in range(len(marks_list1)):
    z = marks_list1[i].rstrip('\n') # remove \n string
    marks_list2.append(z.split(',')) # create two d array
    

for j in range(len(marks_list2)):
    total_marks+=eval(marks_list2[j][1]) 
    k+=1
    marks.append(eval(marks_list2[j][1]))
    
# Mean
mean = total_marks/k
print('The average is:','{0:.{1}f}'.format(mean,2))

# Standard Deviation 
sta_dev=0     
failed_list=('')  

for m in range(len(marks)):   
    sta_dev+=(marks[m]-mean)**2
    sd=math.sqrt(sta_dev/k)
    
print('The std deviation is:','{0:.{1}f}'.format(sd,2))
failed_list=('')

if sd>0:
    print('List of students who need to see an advisor:')

    for c in range(len(marks_list2)):
        if eval((marks_list2[c][1]))< (mean-sd):
            failed_list+=(marks_list2[c][0])+'\n'
    print(failed_list)
        

