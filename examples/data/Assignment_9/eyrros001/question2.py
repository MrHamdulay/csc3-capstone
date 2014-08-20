"""reformat a text file so that all lines are at most a given length
Ross Eyre
11/05/2014"""

fName = input("Enter the input filename:\n")
outName = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))


fileIn = open(fName, 'r')
lines = fileIn.readlines()
fileIn.close()

# take off ends
for i in range (len (lines)):
    if(lines[i]=='\n'):
        lines[i+1]=lines[i+1][0:]
    else:
        lines[i] = lines[i][:-1]
    
#make one long line
string = ''
for i in lines:
    string+=i + " "

#add new lines according to width

def newLines(s):
    l = len(s)
    count = 0
    if(l==0):
        return ""
    else:
        space = s[:width].rfind(" ")
        return s[:space] + "\n" + newLines(s[space+1:])

        
string = newLines(string)    
    
#write to new file
outFile = open(outName, 'w')
print(string, file=outFile)
outFile.close()