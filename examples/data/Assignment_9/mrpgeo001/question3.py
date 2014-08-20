"""Program to check if a sudoku grid is valid
Geoff Murphy
MRPGEO001
15 May 2014"""

line_1 = input('')      #Takes the input for each line
line_2 = input('')
line_3 = input('')
line_4 = input('')
line_5 = input('')
line_6 = input('')
line_7 = input('')
line_8 = input('')
line_9 = input('')

lines = []              #The 2-D array which will be used
line1 = []              #These are the individual arrays which will be put into the main array
line2 = []
line3 = []
line4 = []
line5 = []
line6 = []
line7 = []
line8 = []
line9 = []


for i in line_1:                #Appends each item to the 2-D array
    line1.append(i)
    
for i in line_2:
    line2.append(i)
    
for i in line_3:
    line3.append(i)
    
for i in line_4:
    line4.append(i)
    
for i in line_5:
    line5.append(i)
    
for i in line_6:
    line6.append(i)
    
for i in line_7:
    line7.append(i)
    
for i in line_8:
    line8.append(i)
    
for i in line_9:
    line9.append(i)
    
lines.append(line1)
lines.append(line2)
lines.append(line3)
lines.append(line4)
lines.append(line5)
lines.append(line6)
lines.append(line7)
lines.append(line8)
lines.append(line9)



valid = 0

'''for j in range(8):
    for i in range(8):
        if lines[j][i] == lines[j+1][i]:
            valid = 0
        elif lines'''

a = 0

for i in range(len(lines)):                 #Checks the validity of the grid
    for j in range(len(lines)):
        a = j
        if str(a) in i and lines[i][j] != j:
            valid = 0                       #Produces 0 if the grid is invalid
            
        
        
        
print(valid)
