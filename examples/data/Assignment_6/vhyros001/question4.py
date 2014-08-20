"""Assignment 6 question 4 Histogram of marks
Ross van der Heyde VHYROS001
20 April 2014"""

marks = input("Enter a space-separated list of marks:\n").split()

cat = ['1', '2+', '2-', '3', 'F']#Store mark catergories
count = [0,0,0,0,0] #Store occurences of each catergory

#Count occurences of each category
for i in marks: # i is value
    i = int(i)
    if i >= 75:
        count[0]+=1
    elif i >=70:
        count[1]+=1
    elif i >=60:
        count[2]+=1
    elif i >=50:
        count[3]+=1
    else:
        count[4]+=1

#Print histogram
output = "{:<2}|"

for i in range(len(cat)): # i is index
    print(output.format(cat[i]), "X"*count[i], sep="")