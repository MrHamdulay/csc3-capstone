def average(fielname):
    f=open(filename,'r')
    lines = f.readlines()
    f.close()
    
    sum_= 0
    for line in lines:
        student=line.split(',')
        sum_+=eval(student[1])
    average= sum_/len(lines)
    if str(average)[-2] ==".":
        return str(round(average,2))+"0"
    return str(round(average,2))

def sd(filename):
    f=open(filename,'r')
    lines = f.readlines()
    f.close()    
    mean = eval(average(filename))
    N=len(lines)
    sdn=0
    for line in lines:
        student=line.split(',')
        sdn+=(eval(student[1]) - mean)**2 
    sd = (sdn/N)**0.5
    if str(sd)[-2] ==".":
        return str(round(sd,2))+"0"
    return str(round(sd,2))

def sa(filename):
    f=open(filename,'r')
    lines = f.readlines()
    f.close()
    advisor= False
    for line in lines:
        student=line.split(',')
        if eval(student[1])< eval(average(filename))-eval(sd(filename)):
            advisor =True
    if advisor:
        print('List of students that need to see the advisor:')
        for line in lines:
            student=line.split(',')
            if eval(student[1])< eval(average(filename))-eval(sd(filename)):
                print(student[0])  

filename= input('Enter the marks filename:\n')
print ('The average is: '+average(filename))
print ('The std deviation is: '+sd(filename))
sa(filename)