"""Student advisor vs marks checker
Vahin Gounden
14/05/14"""

#import useful modules
import math

#Create variable for filename
testx = input("Enter the marks filename:\n")

#open, read and close file
f = open(testx, "r")
fl = f.readlines()
f.close

#create lists
lst = []
lst2 = []

#remove the \n element and add items to lst
for line in fl:
    line = line.replace("\n","")
    lst.append (line)

#split items into the name and the mark parts    
for i in range (len(lst)):
    x = lst[i].split (",")
    lst2.append (x)
    
counter = 0

#count the amount of entries
for j in range (len(lst2)):
    counter += 1

su = 0

#find the average
for k in range (len(lst2)):
    x = eval(lst2[k][1])
    su = su + x
    
ave = (round(su/counter,2))
print("The average is:","{0:0<5}".format(ave))

e = 0

#find the stanard deviation
for h in range (len(lst2)):
    t = eval(lst2[h][1])
    r = (t - ave)**2
    e = e + r
    
y = (e/counter)

stddev = (round(math.sqrt(y),2))

if stddev != 0:
    print("The std deviation is:",stddev)
    print("List of students who need to see an advisor:")
    #find the student s that need to see a student advisor
    for c in range (len(lst2)):
        g = eval(lst2[c][1])
        if g < (ave - stddev):
            print(lst2[c][0])  
            
elif stddev == 0:
    print("The std deviation is: 0.00")
    
