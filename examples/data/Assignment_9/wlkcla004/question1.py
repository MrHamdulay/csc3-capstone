"""question1
clare walker
11 may 2014"""
import math

file = open(input("Enter the marks filename:\n"), "r")
markdict={}
marklist=[]
for line in file.readlines():
    entry = line[:-1].split(',')
    markdict[entry[0]] = eval(entry[1])
    marklist.append(entry)
    
    
#get average (sum of all values)
numbers=markdict.values()
sumNumber=0
for number in numbers:
    sumNumber+=number
average=sumNumber/len(numbers)

#calculate std dv
#first get denominator using loop
denominator = 0
for number in numbers:
    denominator+=((number - average)**2)
# full calculation
stdDev=math.sqrt((denominator)/len(numbers))

# calculate mark recommended to see advisor
lowmark=average-stdDev

#new array only entries below lowmark
toBadvised=[]
for i in range(len(marklist)):
    if eval(marklist[i][1]) < lowmark:
        toBadvised.append(marklist[i])
        
#process information as output
print("The average is: {0:.2f}\nThe std deviation is: {1:.2f}".format(average, stdDev))
if len(toBadvised) > 0:
    print("List of students who need to see an advisor:")
    for name in toBadvised:
        print(name[0])
    
        