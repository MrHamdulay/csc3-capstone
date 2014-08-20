#Assignment 9, Question 1
#James Nevin
#11 May 2014

marks_file = input ("Enter the marks filename:\n") #Getting the file name
marks_list = [] #Making a list for the file
f = open (marks_file, "r") #Opening to read
for line in f:
    marks_list.append(line.split(",")) #Adding each line to list
f.close() #Close file
total = 0
number_marks = 0 #Total marks and number of marks
for item in marks_list:
    string = item[1] #Marks part of list
    total += int(string)
    number_marks += 1 #Increase total and number of marks
average = "{:.2f}".format(total/number_marks)
print ("The average is: " + average) #Printing rounded average
dev = 0
for items in marks_list:
    dev += (int(items[1]) - float(average))**2 #Calculating standard deviation
dev = "{:.2f}".format((dev/len(marks_list))**(1/2))
print ("The std deviation is: " + dev) #Printing rounded standard deviation
header = False
for items in marks_list:
    if (int(items[1]) < float(average) - float(dev) and not header): #If mark is less than mean less on standard deviation and no header printed
        print ("List of students who need to see an advisor:")
        print (items[0])
        header = True
    elif (int(items[1]) < float(average) - float(dev)):
        print(items[0])
