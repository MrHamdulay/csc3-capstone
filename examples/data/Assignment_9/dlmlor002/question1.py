"""Program to analyse student marks read in from a file and determine which students need to see a student advisor
Lorena Dal Maso
14 May 2014"""

filename = input("Enter the marks filename:\n")

f = open(filename,"r")

test = f.readline()

array = []
temp = []
while test != "":
    temp = test.split(",")
    array.append(temp)
    test= f.readline()
    
total = 0
for i in range (len(array)):
    numbers = array[i][1]
    total += eval(numbers)

average = total/len(array)
print ("The average is: ",'%0.2f' %(average),sep="")

stdn = 0
for j in range(len(array)):
    step1 = (eval(array[j][1]) - average)**2
    stdn += step1
    ave_std = stdn/len(array)
    std = (ave_std)**(1/2)

print ("The std deviation is: ",'%0.2f' %(std),sep="")

def funct():
    print ("List of students who need to see an advisor:")
    return 1
stop=0
for i in range (len(array)):
    if eval(array[i][1]) < (average - std):
        if stop==0:
            stop=funct()
        print (array[i][0])
    
f.close()
