# program to reformat a text file so that all lines are at most a given length
# 17 May 2014
#JHLBHI001

def readF(filename):
    #read lines in the file, remove new line escape sequences and return all contents as a list
    newLines = []
    file = open(filename,"r")
    lines = file.readlines()
    file.close()
    for line in lines:
        newLines.append(line.replace('\n',''))
    return newLines

def setLines(l,w):
    s = ''
    tmpL = ['']
    i = 0
    for line in l:
        if len(line) > 1:
            words = line.split(' ')
            for word in words:
                if (len(tmpL[i])+len(word)) <= w :
                    tmpL[i] += word+" "
                elif word == 'a':
                    tmpL[i] += word
                else:
                    tmpL.append(word+" ")
                    i += 1
        else:
            tmpL.append('\n')
            i += 1
    return tmpL
def writeF(filename,lines):
    #write contents of outList to output file
    f = open(filename,'w')
    for line in lines:
        print(line,file=f)
    f.close()    

def main():
    inputF = input("Enter the input filename:\n")
    outputF = input("Enter the output filename:\n")
    wid = eval(input("Enter the line width:\n"))
    
    lines = readF(inputF)
    lines = setLines(lines,wid)
    writeF(outputF,lines)

main()
