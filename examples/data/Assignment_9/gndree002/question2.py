"""Program to reformat a text file so that all lines are at most a given length
Reece Gounden
GNDREE002"""


#opens files for reading and writing and prompts user to enter column width
fInput=open(input("Enter the input filename:\n"),"r")
fOutput=open(input("Enter the output filename:\n"),'w')
width=eval(input("Enter the line width:\n"))
ln=''

#Method splits the text in the file into an array by line then puts ###### at paragraph breaks in array
def ReadSplit(fInput):
    lines=list()
    for line in fInput:
        lines.append(line)
    for i in range(len(lines)):
        lines[i]=lines[i][0:len(lines[i])-1]
    fInput.close()
    for i in range(len(lines)):
        if lines[i]=='':
            lines[i]='########'
    lines=' '.join(lines) #spacing between words
    lines=lines.split(' ')
    return lines #returns array of words with paragraph breaks and spacing

#fuction to format the array correctly to be outputted according to user inputted width
def printParagraphs(arrStr):
    arrStr.append('##END##') #appends string to end of array so the end of string can be checked for
    out=list()
    global ln
    i=0
    while arrStr[i]!='##END##':
        if arrStr[i]=='########':
            out.append(ln[0:-1])
            ln=''
            out.append('')
            i+=1    
        else:
            if len(arrStr[i]+ln+' ')<=width+1:
                ln+=arrStr[i]+' '
                i+=1
            else:
                out.append(ln[0:-1])
                ln=arrStr[i]+' '
                i+=1
    out.append(ln)
    return out           

#use of defined functions to read from file and format data
sSplit= ReadSplit(fInput)
out=printParagraphs(sSplit)

#prints each line in 'out' to text file
for i in out:
    print(i,file=fOutput)

fOutput.close()