#a program to format 
#lebogang masila
#16 may 2014



def readF(filename):
    #read lines in the file,and replace new line with an empty string and then return
    newList = []
    file = open(filename,"r")
    lines = file.readlines()
    file.close()
    for line in lines:
        newList.append(line.replace('\n',''))
    return newList

def setLines(l,w): #a function to set the width of the lines
    s = ''
    tmpL = ['']
    i = 0
    for line in l: #loop through the whole list
        if len(line) > 1:
            words = line.split(' ')
            for word in words: #loop through words
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

def main(): #a function which calls all other functions
    inputF = input("Enter the input filename:\n")
    outputF = input("Enter the output filename:\n")
    wid = eval(input("Enter the line width:\n"))
    
    lines = readF(inputF) 
    lines = setLines(lines,wid)
    writeF(outputF,lines)

main()