'''Python Grade checker
sithembiso mashinini
16 May 2014'''

import math

filename = input('Enter the marks filename:\n')#prompts the user for input name txt file 
fob = open(filename,'r')
file_lines = fob.readlines()
fob.close()

lines = file_lines
for i in range(len(lines)-1):# slice the last character of string 
    lines[i] = lines[i][:-1]


summation = 0
for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    summation += int(lines[i][-1])
average = summation/len(lines)# evaluates the average 




summation = 0

for i in range(len(lines)):
    summation += (int(lines[i][-1])- average)**2#formula for standard div
    
  
dev = math.sqrt( summation/len(lines) )





for i in range(len(file_lines)-len(lines)):
    file_lines[i] = file_lines[i][:-1]
    


print('The average is: {:.2f}'.format(average))
print('The std deviation is: {:.2f}'.format(dev))



constant= 1
difference = average - dev



for a in range(len(file_lines)):#checks whicstudent need to an advisor
    fline = int(file_lines[a][-1])
    if fline < difference:
        for b in range(constant):
            print('List of students who need to see an advisor:')
            constant = 0
        print(file_lines[a][0])
        
