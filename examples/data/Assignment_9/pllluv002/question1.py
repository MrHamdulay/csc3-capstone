"""Analysis of marks
Luveshen Pillay
10/5/14"""

#Opening file for proessing
filename=input("Enter the marks filename:\n")
f=open(filename,"r")

#Acquiring average
marksum=0
lines=0
for line in f:
    listline = line.split(",")
    marksum+=eval(listline[1][:-1])
    lines+=1
    
f.close
avg=marksum/lines
print("The average is: {0:0.2f} ".format(avg))

#Calculating SD
SDcount=0
c=open(filename,"r")

for line in c:
    listline = line.split(",")
    SDcount+=((eval(listline[1][:-1])-avg)**2)
c.close()    
SD=(SDcount/lines)**0.5

print("The std deviation is: {0:0.2f}".format(SD))

#Looking for DPR peeps
DPR= avg - SD
z=open(filename,"r")
namelist=""
for line in z:
    listline = line.split(",")
    if eval(listline[1][:-1]) < DPR:
        namelist+=(listline[0]+"\n")
        
if namelist !="":
    print("List of students who need to see an advisor:")
    print(namelist)




