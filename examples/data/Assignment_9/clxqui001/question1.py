#CLXQUI001

total = 0
ALL_SD = 0
marks = []
name = []


import math
file_input = input("Enter the marks filename:\n")
def first ():
    infile = open(file_input, "r")
    info = infile.read()
    counter=info.count(",")
    infile.close()
    return(counter)
number_stu = first()    
count = 0







infile = open(file_input, "r")
for i in range(number_stu):
    info = infile.readline()
    count = float(info[info.find(",")+1:])
    total = total + count
    marks.append(count)
    name.append(info)
    
the_average = total/number_stu






for i in marks:
    sd = float(i) - the_average
    sd2 = sd**2
    ALL_SD = ALL_SD + sd2
    
fsd = (math.sqrt(ALL_SD/number_stu))







print("The average is:", "{:.2f}".format(the_average))
print("The std deviation is:","{:.2f}".format(fsd))






if number_stu>1:
    print("List of students who need to see an advisor:")
for i in name:
    if number_stu ==1:
        p=1
    elif int(i[i.find(",")+1:]) <= the_average-fsd:
        print(i[:i.find(",")])