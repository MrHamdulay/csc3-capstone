#Assignment 9.1
#Michael Gant
#11/05/2014

import math

#Mark analyser
    

arrNames = []
arrMarks = []
iMean = 0
iStanDev = 0
bPrinted = False

fMarks = open(input("Enter the marks filename:\n"), "r")
for k in fMarks:
    sLine = k
    if sLine[-1] == "\n":
        sLine = sLine[0:-1]
    iPos = sLine.index(",")
    arrNames.append(sLine[0:iPos])
    iMark = int(sLine[iPos+1:])
    iMean = iMean + iMark
    arrMarks.append(iMark)
iMean = iMean / len(arrMarks)

for k in arrMarks:
    iStanDev = iStanDev + (k-iMean)**2
iStanDev = math.sqrt(iStanDev/len(arrMarks))

print("The average is: %.2f" % round(iMean, 2))
print("The std deviation is: %.2f" % round(iStanDev,2))

for k in range(len(arrMarks)):
    if arrMarks[k] < iMean - iStanDev:
        if bPrinted == False:
            bPrinted = True
            print("List of students who need to see an advisor:")
        print(arrNames[k])





fMarks.close()