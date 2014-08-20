#Kimberley Naidoo
#20 april 2014
#Histogram that refelects marks

#Enter the marks
catergories = ["1 ", "2+", "2-", "3 ", "F "]
counters = ['', '', '', '', '']
marks=input("Enter a space-separated list of marks:\n").split()

for i in range(len(marks)): #Convert string data to integers
    marks[i] = eval(marks[i])

#Test which category each mark falls in and add one X to that category
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
    print(catergories[i], "|", counters[i], sep = "") #Print both the labels and counter lists

