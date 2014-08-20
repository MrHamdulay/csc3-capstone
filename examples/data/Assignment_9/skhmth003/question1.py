import math
def calc():
    """Function that calculates the average and standard deviation from a file"""
    global new_marks
    global average
    global std_dev
    global new_names
    filename=input("Enter the marks filename:\n")
    infile=open(filename, "r")
    lines=infile.readlines()
    name_list=[]
    new_lines=[]
    new_marks=[]
    new_names=[]
    #removing \n character
    for i in lines:
        if i!=lines[-1]:
            i=i[:-1]
            new_lines.append(i)
        else: new_lines.append(i)
    #seperating marks from names
    for i in new_lines:
        j=i.find(",")
        names=i[:j]
        marks=i[j+1:]
        new_names.append(names)
        new_marks.append(marks)
    #Calculating the sum
    summation=0
    for i in new_marks:
        summation+=eval(i)
    #Average 
    average=summation/len(new_marks)
    #Standard Deviation
    sum_square=0
    for i in new_marks:
        sum_square+=(eval(i)-average)**2
    std_dev=math.sqrt(sum_square/len(new_marks))
def student():
    """function that finds students that need to see an advisor"""
    global student_advisor
    student=[]
    student_advisor=[]
    j=0
    for i in new_marks:
        test=(average-std_dev)
        if eval(i)<test:
            student.append(j)
        j+=1
    for i in student:
        student_advisor.append(new_names[i])
def main():
    calc()
    student()
    print("The average is:", ("{0:.2f}".format(round(average,2))))
    print("The std deviation is:", "{0:.2f}".format(round(std_dev,2)))
    if std_dev>0:
        print("List of students who need to see an advisor:")
        for i in student_advisor: 
            print(i)
main()