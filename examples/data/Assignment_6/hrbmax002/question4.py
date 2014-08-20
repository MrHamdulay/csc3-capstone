marks = input("Enter a space-separated list of marks:\n")

listMarks = list(marks.split(" "))
currentMark = 0

dict1 = {"1 ":"|", "2+":"|", "2-":"|", "3 ":"|", "F ":"|"}

for i in range (len(listMarks)):
    currentMark = eval(listMarks[i])
    if currentMark < 50:
        dict1["F "] = dict1["F "] + "X"
    elif currentMark >= 50 and currentMark < 60:
        dict1["3 "] = dict1["3 "] + "X"
    elif currentMark >= 60 and currentMark < 70:
        dict1["2-"] = dict1["2-"] + "X"
    elif currentMark >= 70 and currentMark < 75:
        dict1["2+"] = dict1["2+"] + "X"
    else:
        dict1["1 "] = dict1["1 "] + "X"


for j,k in sorted(dict1.items()):
    print (j + k )



    
