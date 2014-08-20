import math
def main():
    a=input("Enter the marks filename:\n")
    filename=open(a,'r')
    std_list=filename.readlines()
    marks_list=[]
    std_name={}
    name_list=[]
    for i in std_list:
        i=i[:-1] 
        line=i.split(',')
        std_name[line[0]]=line[1]
        marks_list.append(line[1])
        name_list.append(line[0])
    total_marks=0
    
    for i in  marks_list:
        total_marks+=int(i)
        
    average=total_marks/len(marks_list)
    print("The average is: {:.2f}".format(average))
    var=0
    
    for i in  marks_list:
        var+=(int(i)-average)**2
    standard_dev=math.sqrt((var)/len(marks_list))
    print("The std deviation is: {:.2f}".format(standard_dev))
    check=0
    for i in name_list:
        if int(std_name[i])<average-standard_dev:
            if check==0:
                print("List of students who need to see an advisor:")
            print(i)
            check=1
        
            
        
        
    
main()
    