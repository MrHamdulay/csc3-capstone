#getting the list aligned to the length of the longest wod
#omphemtse molusi
#MLSOMP001
#25 APRIL 2014

labels = ["1 ", "2+", "2-", "3 ", "F "]
count = ['', '', '', '', '']

points = input("Enter a space-separated list of marks:\n").split() #spliting the input

for i in range(len(points)): 
    points[i] = eval(points[i])


for mark in points: 
    if mark >= 75:
        count[0] += "y"  #categorising marks
    elif mark >= 70:
        count[1] += "y"
    elif mark >= 60:
        count[2] += "y"
    elif mark >= 50:
        count[3] += "y"
    else:
        count[4] += "y"
        
for i in range(len(labels)):
    print(labels[i], "|", count[i], sep = "") #output with separated arrays
        
