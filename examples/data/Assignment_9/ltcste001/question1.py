#stephanie latchmanan
#Assignment 9 (calculate standard deviation of marks
#10 May 2014
import math

filename = input("Enter the marks filename:\n")       #get filename
f = open(filename, "r")                               #open file and readlines into list
lines = f.readlines()
f.close()                                             #close file

# chop off the trailing carriage returns
for i in range (len (lines)):
    lines[i] = lines[i][:-1]

#calculate the mean
total = 0
for i in range(len(lines)):
    if lines[i][-2] == ",":
        total += int(lines[i][-1:])
    else:
        total += int(lines[i][-2:])                      #add last 2 digits for each item in list
mean = total/len(lines)                              #calculate mean by dividing total by number of students

#calculate the standard deviation
total1 = 0
for i in range(len(lines)):
    if lines[i][-2] == ",":
        total1 += (int(lines[i][-1:])-(total/len(lines)))**2
    else:
        total1 += (int(lines[i][-2:])-(total/len(lines)))**2            #add the squares of mean less each data value for each student
std_dev = math.sqrt(total1/len(lines))                              #square root of the total divided by the number of students

print("The average is:", "{0:0<5}".format(round(mean,2)))
print("The std deviation is:", "{0:0<4}".format(round(std_dev,2)))    #format to get an extra 0 after standard deviation and mean

count = 0
for i in range(len(lines)):                                          #if student's mark is less than one standard deviation of mean print name
    if lines[i][-2] == ",":
        if int(lines[i][-1:]) < (mean - std_dev):
            if count == 0:
                print("List of students who need to see an advisor:")
                count += 1
            print(lines[i][:-2])
    elif int(lines[i][-2:]) < (mean - std_dev):
        if count == 0:
            print("List of students who need to see an advisor:")
            count += 1
        print(lines[i][:-3])