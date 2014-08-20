""""Program to format text from one file and paste it in another file
Given Moyo
19 May 2014"""


def readF(filename):
    # to read lines in the file, remove new line,escape sequences and return all contents as a list
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
    #to write contents of outList to the output file
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
