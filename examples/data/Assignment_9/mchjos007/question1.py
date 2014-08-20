"""code to read from a file and print names of students with marks one standard deviation lower than the mean"""
file = input("Enter the marks filename:\n")
f = open (file, "r")
counter = 0.0
thestuff = []
for line in f:
    counter += 1.0
    thestuff.append(line.split(","))
f.close
mean = 0.0
for i in range(int(counter)):
    mean += float(thestuff[i][1])
mean = mean/counter
stndrddvtn = 0.0
for i in range(int(counter)):
    stndrddvtn += ((float(thestuff[i][1]) - mean)**2)
stndrddvtn = (stndrddvtn/ counter)**0.5
print("The average is:", "%.2f" % mean)
print("The std deviation is:", "%.2f" % stndrddvtn)
doesanybodyneedtutoring = False
for i in range(int(counter)):
    if float(thestuff[i][1])<(mean-stndrddvtn):
        doesanybodyneedtutoring = True
if doesanybodyneedtutoring:
    
    print("List of students who need to see an advisor:")
    for i in range(int(counter)):
        if float(thestuff[i][1])<(mean-stndrddvtn):
            print(thestuff[i][0])