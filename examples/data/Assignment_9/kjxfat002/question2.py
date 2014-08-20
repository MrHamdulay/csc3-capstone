"""
Created on May 15th 2014
Reformatting a text file
KJXFAT002

"""

inputFile = input("Enter the input filename:\n")
outputFile = input("Enter the output filename:\n")
widthOfLines = eval(input("Enter the line width:\n"))

readFile = open(inputFile,"r")
writeFile = open(outputFile, "w")

#read every line into a string x
x = readFile.read()

#removing new lines from string
x = x.replace("\n","")

newx = []
counter = widthOfLines
   
#list newx - each line will be stored in one element of the list newx

while True:
    
    if len(x) < counter:
        newx.append(x)
        break
    
    if x[counter] == " ":
        newx.append(x[0:counter])
        x = x[counter:]
        counter = widthOfLines
        
    else:
        counter =  counter - 1 
        

# remobing initial space from each element 
for i in range(1,len(newx)):
    a = newx[i]
    a = a[1:]
    newx[i] = a


for i in range(len(newx)):
    print(newx[i])    
    
for i in range(len(newx)):
    writeFile.write(newx[i])
    writeFile.write("\n")
    
    

    
writeFile.close()
readFile.close()
        
    





