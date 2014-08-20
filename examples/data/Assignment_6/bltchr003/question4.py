"""User enters marks, program then prints out marks in the form of a histogram in grade catagories
Chris Bolton """

marks = input("Enter a space-separated list of marks:\n")

list_marks = list(marks.split(" ")) #marks are entered into list, split whereever there is a space
current_Mark = 0

dict1 = {"1 ":"|", "2+":"|", "2-":"|", "3 ":"|", "F ":"|"}

for i in range (len(list_marks)): #loop to catagorize the inputed marks
    current_Mark = eval(list_marks[i])
    if current_Mark < 50:
        dict1["F "] = dict1["F "] + "X"
    elif current_Mark >= 50 and current_Mark < 60:
        dict1["3 "] = dict1["3 "] + "X"
    elif current_Mark >= 60 and current_Mark < 70:
        dict1["2-"] = dict1["2-"] + "X"
    elif current_Mark >= 70 and current_Mark < 75:
        dict1["2+"] = dict1["2+"] + "X"
    else:
        dict1["1 "] = dict1["1 "] + "X"


for i,t in sorted(dict1.items()): 
    print (i + t )