#Histogram
#Devaksha Pillay
#21 April 2014

marks = input("Enter a space-separated list of marks: \n")
marks = marks.split(" ")
eval_marks = []
grade = [0,0,0,0,0]

#convert strings to numbers
for i in range (len(marks)):
    newmarks = eval(marks[i])
    eval_marks.append(newmarks)

#determine which category each mark falls into
for i in range (len(marks)):
    if eval_marks[i] >= 75:
        grade[0] +=1
    elif 70 <= eval_marks[i] < 75:
        grade[1] +=1
    elif 60<= eval_marks[i] < 70:
        grade[2] +=1
    elif 50 <=eval_marks[i] < 60:
        grade[3] +=1
    elif eval_marks[i] < 50:
        grade[4] +=1
 
#print out histogram        
print("1 |", "X"*grade[0], sep = "")
print("2+|","X"*grade[1], sep ="")
print("2-|","X"*grade[2], sep ="")
print("3 |","X"*grade[3], sep ="")
print("F |","X"*grade[4], sep ="")