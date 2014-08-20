'''program to give the average, the standard deviation and those who need to see a student advisor
Othniel KONAN
KNNOTH001
10 May 2014'''

from math import*
     
#PROMPT USER
the_file = input('Enter the marks filename:\n')

#PUT ALL NAMES AND MARKS IN A GRID
grid=[]
with open(the_file,'r') as f:           #open the file and close it when all instruction are excecuted
    for line in f:                      #go through each line in the file
        line = line.split(',')          #remove the backspace at the end of each line and split the line
        grid.append(line)               #append the line to the grid

#CALCUL OF THE MEAN
total = 0
for i in range(len(grid)):              #go throuth the grid 
    total += int(grid[i][1])            #add the mark to the total(note that the '\n' at the end of grid[i][1] is removed as we convert it to int)
mean = total / (i+1)                    #calculate the mean 

#CALCULATION OF THE STANDARD DEVIATION
total = 0
for i in range(len(grid)):
    total += pow(int(grid[i][1])-mean,2)    #sum of the each (mark-mean)square 
sd = sqrt(total/(i+1))                      #calcul of the standard deviaton


#GIVE PART OF THE OUTPUT
print('The average is: {0:3.2f}'.format(mean))
print('The std deviation is: {0:3.2f}'.format(sd))

#PRINT NAME OF THOSE WHO NEED TO SEE THE ADVISOR
l=[]
prt=False
for i in range(len(grid)):
    if int(grid[i][1]) < mean-sd:                           #check if anyone has a mark bellow the requirement
        prt = True                                          #change parameter to true
        l.append(grid[i][0])                                #append ther name to the list
if prt == True:                                             #check if someone need to see the advisor
    print('List of students who need to see an advisor:')
    for i in l:                                             #print their name
        print(i)