'''Program to analyse student marks read in from a file and determine which students need to see a student advisor.
GNDREE002. 
Reece Gounden'''

# open, read and close the file
file = open (input("Enter the marks filename:\n"), "r")
arrF=file.readlines()
file.close()

#Define variables
arrNums=list()
mean=0
stddev=0
arrIdiots=list()

#take away the \n regex
for i in range (len (arrF)-1):
    arrF[i] = arrF[i][:-1]

#calculate the mean
for i in range(len(arrF)):
    mean+=int(arrF[i][arrF[i].find(',')+1::])
    arrNums.append(int(arrF[i][arrF[i].find(',')+1::]))    
mean=mean/len(arrF)
print("The average is: "+"%0.2f" % (mean))

#calculate the Std Deviation
for i in arrNums:
    stddev+=((i-mean)**2)
stddev=(stddev/len(arrNums))**(1/2)
print("The std deviation is: "+"%0.2f" % (stddev))

#Checks for and adds people who need to see an advisor to the list, prints the list if its greater than 0
for i in range(len(arrF)):
    if arrNums[i]<(mean-stddev):
        arrIdiots.append(arrF[i][0:arrF[i].find(',')])
if len(arrIdiots)>0:
    print("List of students who need to see an advisor:")
    for i in arrIdiots:
        print(i)