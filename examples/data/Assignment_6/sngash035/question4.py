#Ashton Singh
#25 April 2014
#Histogram reflecting marks

#Entering the marks
catergories = ["1 ", "2+", "2-", "3 ", "F "]
counters = ['', '', '', '', '']
marks=input("Enter a space-separated list of marks:\n").split()

for i in range(len(marks)): #Converting string data to integers
    marks[i] = eval(marks[i])

#Testing which category each mark falls in and adding X to that category
for mark in marks: 
    if mark >= 75:
        counters[0] += "X"
    elif mark >= 70:
        counters[1] += "X"
    elif mark >= 60:
        counters[2] += "X"
    elif mark >= 50:
        counters[3] += "X"
    else:
        counters[4] += "X"
        
for i in range(len(catergories)):
    print(catergories[i], "|", counters[i], sep = "") #Printing both the lists with labels and counters
