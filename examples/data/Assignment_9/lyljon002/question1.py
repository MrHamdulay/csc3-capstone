#10 May 2014   
#Program to show average, std deviation and advisor meets from a textfile
#LYLJON002

import math

filename = input("Enter the marks filename:\n")

f = open(filename)
contents = f.read()
f.close()


count = 0
total = 0

for string in contents.split("\n"):
    if "," in string:
        number = int(string.split(",")[1])      #get the number
        total = total + number
        count = count + 1
    average = total / count         #calculate the average
    
total = 0

for string in contents.split("\n"):
    if "," in string:
        number = int(string.split(",")[1])          #get the number
        total = total + ((number - average)**2)


stddeviation =  math.sqrt(total / count)        #calculate std deviation


print("The average is:", "%.2f" % (average), sep = ' ')
print("The std deviation is:", "%.2f" % (stddeviation), sep = ' ')      #output

namelist = ''
count = 0

for string in contents.split("\n"):
    if "," in string:
        number = int(string.split(",")[1])              
        if number < (average - stddeviation):                   #get name list
            count = count + 1
            namelist = namelist + (string.split(",")[0]) + "\n"
    
if count > 0:
    print("List of students who need to see an advisor:")       #output namelist
    print(namelist)
    
        
        
