import math

lines = []

# this will have to be changed to open a .txt file

file = input("Enter the marks filename:\n")

f = open(file,"r")

namelist = []
both_list = []
rank = []
totalmark = 0
counter = 0
for line in f.readlines():
    #prin(line, end="")
    namesplit = line.split(",")
    #print(namesplit)
    mark = namesplit[1]
    rank.append(eval(mark))    
    #print(mark)
    totalmark = totalmark + eval(mark)
    both_list.append(namesplit)  
    counter += 1
    
averagemark = totalmark/counter
print("The average is:",round(averagemark,2))
#print(rank)

rank_var = 0
counter = 0
for i in range(len(rank)):
    rank_var += (rank[i]-averagemark)**2
    counter += 1
    
#print("variance is: ",rank_var)

rank_std = math.sqrt(rank_var/counter)

print("The std deviation is:",round(rank_std,2))

print("List of students who need to see an advisor:")

#print(both_list)

for i in range(len(both_list)):
    if int(both_list[i][1]) < averagemark - rank_std:
        print(both_list[i][0])

f.close()