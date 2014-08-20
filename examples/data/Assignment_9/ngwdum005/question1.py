'''Dumisani Ngwenza
NGWDUM005
10/05/2014
Assignment 8'''
import math

#require input from user
filename = input('Enter the marks filename:\n')

#open the file
f = open(filename, "r")
#counting the number of students
N = 0
for i in f:
    N += 1
f.close()


#re-open file
f = open (filename, "r")
#calculating mean
sum = 0
line = f.readline()
while line != '':
    find_comma = line.find(',')
    mark = int(line[find_comma+1:-1])
    sum+=mark
    line = f.readline()
mean = round((sum/N), 2)
f.close()


#re-opening file
f = open (filename, "r")
#calculating standard deviation
variation = 0
line = f.readline()
while line!= '':
    find_comma = line.find(',')
    mark = int(line[find_comma+1:-1])
    variation += (mark - mean)*(mark - mean)
    line = f.readline()
std_deviation = round(math.sqrt(variation/N), 2)
f.close()

print ('The average is:', mean)
print ('The std deviation is:', std_deviation)
#print ('List of students who need to see an advisor:')

#re-open the textfile
f = open (filename, "r")
#determining which students need to see the teacher
benchmark = mean - std_deviation
line = f.readline()
while line !='':
    find_comma = line.find(',')
    mark = int(line[find_comma+1:-1])
    if mark < benchmark:
        print ('List of students who need to see an advisor:')
        print (line[:find_comma])
    line = f.readline()
f.close()