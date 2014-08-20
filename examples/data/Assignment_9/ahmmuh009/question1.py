import math
def marks():
    list_marks=[]
    variance=0
    filename=input("Enter the marks filename:\n")
    f=open(filename,'r')
    for line in f:
        name,mark=line.split(",")
        list_marks.append(float(mark))
    average=(float(sum(list_marks))/len(list_marks))+0.0000000001
    for mark in list_marks:
        variance+=(pow(((float(mark)-average)),2))
    standard_dev=round(math.sqrt(variance/(len(list_marks)-1)),2)
    advisor=average-standard_dev
    if str(average)[3]=="0":
        average=round((average),2)
        print("The average is:",str(average)+"0")
    else :
        round((average),2)
        print("The average is:",round((average),2))
    print("The std deviation is:",standard_dev)
    print("List of students who need to see an advisor:")
    for line in f:
        name,mark=line.split(",")
        if mark<advisor:
            print(name)
    f.close()
marks()
        
    
    