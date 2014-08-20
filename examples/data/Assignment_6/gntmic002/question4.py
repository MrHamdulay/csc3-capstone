#Assignment 6.3
#Michael Gant
#20/04/2014

#Grades counter

sline = ""
arrGrades = [101,75, 70, 60, 50, 0] #constraints for the symbols
arrGradesSym = ["1 ", "2+", "2-", "3 ", "F "]
arrMarks = input("Enter a space-separated list of marks:\n").split(" ") #recieving input and assignint to an array

for k in range(1,5+1):
    sline = "|"
    for j in arrMarks:
        if (int(j) >= arrGrades[k]) and (int(j) < arrGrades[k-1]): #checks that the mark is within the constraint
            sline = sline + "X"
    print(arrGradesSym[k-1] + sline)
        