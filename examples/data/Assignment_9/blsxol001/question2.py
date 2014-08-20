# A program to format a file to user specification
# xola bILOSE

#13-05-2014

# opening file for reading

file = input("Enter the input filename:\n")
outputfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

file1= open(file,"r")
lines = file1.readlines()
file1.close()
# creating new file

file2 = open(outputfile, 'w')

startpoint = 0
string = ""

for i in range(len(lines)):
    newline = lines[i].replace("\n","")
    if newline == "":
        file2.write(string+"\n")
        file2.write("\n")
        string = ""
        starpoint = 0
    elif (startpoint + len(newline)) > width:
#split each line to mark and name
            texts = newline.split(" ")
            textlength=len(texts[i])
            for i in range(len(texts)):
                startpoint += len(texts[i]) +1
#this  prevents the cutting of words
                if startpoint > width + 1:
                    startpoint = len(texts[i]) + 1
                    
                    file2.write(string+"\n")                
                    string = ""
                if string == "":
                    string += texts[i]
                else:
                    string += " "+texts[i]
    
    else:
        file2.write(newline+"\n")
else:
    if string != "":
        file2.write(string+"\n")

#close the file 
file2.close()
