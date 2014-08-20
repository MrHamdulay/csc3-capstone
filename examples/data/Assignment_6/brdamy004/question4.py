# Assignment 6 question 4
# Amy Brodie
# 25/04/2014

marks = input("Enter a space-separated list of marks:\n")
marks_list = [["1",0],["2+",0],["2-",0],["3",0],["F",0]]

# separate marks into categories
while marks:
    pos = marks.find(" ")
    if pos == -1:
        one_mark = eval(marks)
        marks = ""
    else:
        one_mark = eval(marks[:pos])
        marks = marks[pos+1:]
    if one_mark >= 75:
        marks_list[0][1] += 1
    elif one_mark >= 70:
        marks_list[1][1] +=1
    elif one_mark >= 60:
        marks_list[2][1] += 1
    elif one_mark >= 50:
        marks_list[3][1] += 1
    else:
        marks_list[4][1] += 1
        
# output histogram
print("1 |","X"*marks_list[0][1],sep="")
print("2+|","X"*marks_list[1][1],sep="")
print("2-|","X"*marks_list[2][1],sep="")
print("3 |","X"*marks_list[3][1],sep="")
print("F |","X"*marks_list[4][1],sep="")