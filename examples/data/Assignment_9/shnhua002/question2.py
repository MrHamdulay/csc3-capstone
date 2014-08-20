'''Question 2 Assignment 9
Charlie Shang
SHNHUA002
2014.05.15'''

infile = open(input("Enter the input filename:\n"),"r")

outfile = open(input("Enter the output filename:\n"),'w')

width = eval(input("Enter the line width:\n"))

def split_file(infile):
    lines=[]
    
    lines = infile.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i][:len(lines[i])-1]
        if lines[i]=='': #if empty item, change it to '---'
            lines[i]='---'
    infile.close()
    
    lines = ' '.join(lines) #joins the lines then splits them to make sure all items are seperate
    lines = lines.split(' ')
    
    return lines
    
    
def print_lines(strList):
    strList.append('-END-') #add marker to end of list
    outList=[] #output list to be returned
    
    line = ''
    i=0
    
    while strList[i] != '-END-':
        if strList[i]=='---': #if 'empty item'
            outList.append(line[:-1])
            line=''
            outList.append('')
            i+=1  #inc the position in the list
        else:
            if len(strList[i]+line+' ') <= width + 1: #if shorter than width then add contents to current line
                line += strList[i] + ' ' 
                i+=1
            else:
                outList.append(line[:-1]) #if Longer, start new a new line
                line = strList[i] + ' '
                i+=1
    
    outList.append(line)
    return outList    
       


arrLines = split_file(infile) #make a list from the input file
output = print_lines(arrLines) #print the list to the width

for i in output: #write to file
    print(i, file = outfile)

outfile.close()