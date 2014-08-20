import math
# define function to find students with low marks
def decider():
    #read the file with marks in lines
    total, count = 0, 0
    file = input("Enter the marks filename:\n")
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    #get student name and mark and get total and number of students
    for line in lines:
        student = line.split(',')
        student[1] =eval(student[1])
        total += student[1]
        count+=1
    average = total/count
    add=0
    #get the sum of the deviations
    for line in lines:
        student = line.split(',')
        student[1] =eval(student[1])
        add+= (student[1]-average)**2
    sd = math.sqrt(add/count)
    pas = average-sd
    fail=[]
    #get list of students with low mark
    for line in lines:
        student = line.split(',')
        student[1] =eval(student[1])
        if student[1]<pas:
            fail.append(student[0])
    
    #print out list of those students and average and std to two decimals

    print('The average is:', '%.2f'%average)
    print('The std deviation is:', '%.2f'%sd)
    if len(fail)>0:
        print('List of students who need to see an advisor:') 
        for i in range(len(fail)):
            print(fail[i])
        
decider()
                   
            