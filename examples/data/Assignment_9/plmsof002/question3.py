#Suduko
#Sofia Palmer
#14 May 2014

f = open(filename, "r")
lines = f.readlines()
f.close ()

row = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        index = lines[i][j]
        if (row[index] == 1):
            #problem
        else:
            row[index] = 1
    

