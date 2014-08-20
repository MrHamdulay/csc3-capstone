# Khyati Jinerdeb
# Assignment 9
# Date: 17.05.2014
# to program a text file to make them of same length


def readF(filename):
    newLines = []         #To create a list
    file = open(filename,"r")   #To open the file
    lines = file.readlines()    #To read lines into a string
    file.close()                #To close the file
    for line in lines:
        newLines.append(line.replace('\n',''))    #To replace all the command for empty lines by an empty string(to remove all \n)
    return newLines                               #To add it to the list also

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
