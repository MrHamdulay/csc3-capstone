"""Student Marks
Sachin Murugan 
12/5/2014"""
import math 
filename =(input("Enter the marks filename:\n"))
#open text file and read lines
f = open (filename, "r")
lines = f.readlines ()
f.close ()

Dict = {}
studlist = []
#remove new line characters from string 
for i in (lines):
    splitlist = i.split(",")
    studlist.append(splitlist[0])
    if "\n" in i:
        Dict[splitlist[0]]=eval(splitlist[1][0:len(splitlist[1])-1])
    else:
        Dict[splitlist[0]]=eval(splitlist[1])
#calculate the mean average of the marks
fields = 0
average = sum(Dict.values())/len(lines)
print ("The average is: {0:.2f}".format(average))
#calculate the standard deviation(2 d.p)
for i in Dict:
    new=(Dict[i] - average)**2
    fields+=new
radicand = fields/len(lines)
StanDev = math.sqrt(radicand)
print ("The std deviation is: {0:.2f}".format(StanDev))


#determine students with marks < 1 s.d below the mean
StudAdv = (average-StanDev)
for i in Dict:
    if StudAdv>Dict[i]:
        print ("List of students who need to see an advisor:")
    break
for j in range(len(studlist)):
    if StudAdv>Dict[studlist[j]]:
        print (studlist[j])




