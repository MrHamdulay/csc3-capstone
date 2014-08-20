
""""a histogram based on given input
tafara mtutu
21 april 2014"""

grades  = []
marks = input("Enter a space-separated list of marks:\n")
mark_list = marks.split(" ")
for i in mark_list:
    if int(i) >= 75:
        grades.append('1 ')
    elif int(i) >= 70:
        grades.append('2+')
    elif int(i) >= 60:
        grades.append('2-')
    elif int(i) >= 50:
        grades.append('3 ')
    else:
        grades.append('F ')
        
#if no grades were in one or more of the categories
grades.append('1 ')
grades.append('2+')
grades.append('2-')
grades.append('3 ')
grades.append('F ')
grades.sort()    

#print out histogram
temp = []
for i in grades:
    if i not in temp:
        print(i,"|", "X"*(grades.count(i)- 1), sep = "")
        temp.append(i)
    else: continue
        
        