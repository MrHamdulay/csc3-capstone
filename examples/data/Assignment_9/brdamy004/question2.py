# Assigment 9 question 2
# Amy Brodie
# 11/05/2014

# initialise variables and get input
ifilename = input("Enter the input filename:\n")
ofilename = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))
inputlist = []
single_line = ""
outputlist = []

# input textfile contents into a list
f = open(ifilename,"r")
inputlist = f.readlines()
f.close()

# remove newline characters and insert list contents into a string variable
for i in range(len(inputlist)):
    pos = inputlist[i].find("\n")
    if inputlist[i] == "\n":
        single_line += inputlist[i]
    elif pos == -1:
        pass
    else:
        inputlist[i] = inputlist[i][:pos]
    single_line += inputlist[i] + " "
    
    
# check length of string against chosen width and format appropriately       
while single_line:
    posn = single_line.find("\n")
    if (len(single_line) < line_width) or (len(single_line) == line_width):
        outputlist.append(single_line)
        single_line = ""
    elif single_line[:line_width][line_width-1] == " ":
        outputlist.append(single_line[:line_width])
        single_line = single_line[line_width:]
    elif single_line[line_width] == " ":
        outputlist.append(single_line[:line_width])
        single_line = single_line[line_width+1:]
    elif (posn<=line_width) and (posn!=-1):
        outputlist.append(single_line[:posn+1])
        single_line = single_line[posn+3:]
    else:
        temp = single_line[:line_width]
        temp = temp[::-1]
        pos = temp.find(" ")
        temp = temp[pos+1:]
        outputlist.append(temp[::-1])
        single_line = single_line[len(temp)+1:]  
    
        
# write formatted list into specified textfile
f = open(ofilename,"w")
for i in range(len(outputlist)):
    print(outputlist[i], file=f)
f.close()