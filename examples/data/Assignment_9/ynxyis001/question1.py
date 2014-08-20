#Studdents who need to see a student advisor
#Jennifer Yuan (YNXYIS001)
#11 May 2014

import math

filename = input("Enter the marks filename:\n") #gets text file name from user

f = open(filename, "r") #opens file to read
list = f.readlines() #puts all lines in text into a list with each line as one item in the list
f.close() #closes text file

for i in range(len(list)): #removes \n from the end of each item in list
    list[i] = list[i][:-1]
    
for i in range(len(list)): #Splits all items in list wherever there is a comma
    list[i] =list[i].split(",")

sum = 0 #accumulator
for i in range(len(list)):
    sum = sum + eval(list[i][1]) #adds eachs person's mark to the accumulator "sum"
    average = sum/len(list) #works out the average
    
marks =[] #empty string
for i in range(len(list)):
        marks.append(list[i][1]) #puts all marks into one list named marks
        
def std_deviation():
    middle = 0 #middle of the standard deviation formula starts off as zero
    for i in range(len(marks)):
        middle = middle + ((eval(marks[i]) - average)**2) 
    std_d = math.sqrt(middle / len(marks))
    return round(std_d, 2) #rounds off standard deviation to two decimal places
    
if sum%len(list)==0: #puts two decimal places after "0"
    new_average= str(average) + "0"
else:
    new_average = round(average,2)

mark= []    #empty string
def advisor():
    bench_mark = average - std_deviation() #if a person has a mark less than one standard deviation below the average, then that person must see an advisor
    for i in range(len(list)):
        if eval(list[i][1]) < bench_mark:
            mark.append(list[i][0]) #if a person has to see an advisor, his name is put into the list, mark
advisor()              
if std_deviation() == 0.0:
    deviation = "0.00" #makes sure that all answers are to two decimal places
else:
    deviation = std_deviation()
    
print("The average is:", new_average)
print("The std deviation is:", deviation)
if  mark != []: #only prints if there are students who need to see an advisor
    print("List of students who need to see an advisor:") 
    for i in mark:
        print(i)