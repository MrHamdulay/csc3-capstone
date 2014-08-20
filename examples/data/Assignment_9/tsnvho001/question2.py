"""Program to reformat a text file so that all lines are at most a given length
Tsanwani Vhonani
12 May 2014"""

def file(filename):
    #read lines in the file and return all contents as a list with no spaces
    list_lines=[]
    file1 = open(filename,"r")
    lines = file1.readlines()
    file1.close()
    for line in lines:
        list_lines.append(line.replace('\n',''))
    return list_lines

def set_lines(a,b):
    #join the lines
    c=''
    d=['']
    e=0
    for line in a:
        if len(line)>1:
            join_lines=line.split(' ')
            for i in join_lines:
                if (len(d[e])+len(i))<=b :
                    d[e]+=i+" "
                elif i=='a':
                    d[e]+=i
                else:
                    d.append(i+" ")
                    e+= 1
        else:
            d.append('\n')
            e+=1
    return d

def new_file(filename,lines):
    #write the contents into a new file
    file2 = open(filename,'w')
    for line in lines:
        print(line,file=file2)
    file2.close()    

def main():
    infile=input("Enter the input filename:\n")
    outfile=input("Enter the output filename:\n")
    width=eval(input("Enter the line width:\n"))
    
    lines=file(infile)
    lines=set_lines(lines,width)
    new_file(outfile,lines)

main()