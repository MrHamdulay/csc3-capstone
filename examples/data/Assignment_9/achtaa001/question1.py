#Taahirah Achmat
import math

f = input("Enter the marks filename:\n")
file = open(f,"r")
lines = file.readlines()
file.close()

for j in range (len(lines)):
    lines[j] = lines[j][:-1]

New_List = []
tot = 0
marks = []

for j in lines:
    New_List.append(j.split(','))
   
for j in range(len(lines)):
    marks.append(New_List[j][1])  

for j in marks:
    tot = tot + eval(j)

average = round(tot/len(New_List), 2)

sd_tot = 0
for j in marks:
    sd_tot = sd_tot + ((eval(j) - average)**2)
standard_dev = round(math.sqrt(sd_tot/len(New_List)),2)

print("The average is:", format(average, ".2f"))
print("The std deviation is:", format(standard_dev, ".2f"))

if standard_dev > 0:    
    print("List of students who need to see an advisor:")
    for j in range(len(marks)):   
        if eval(New_List[j][1]) < (average - standard_dev):
            print(New_List[j][0])
        else:
            None