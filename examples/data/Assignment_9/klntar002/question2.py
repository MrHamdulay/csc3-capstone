""" Tarisai Kalinde
student number: klntar002
program to reformat text"""



""" function to access file of input"""
def read(filename):
    f=open(filename,"r")
    lines = f.readlines()
    f.close()
    return lines

""" function to format string to a certain width"""
def reformat(lines, w):
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')    # replacing new line characters with empty strings
        
    array=['']                                  # array to accumulate paragraph, line by line
    j = 0                                       # counter
    for line in lines:
        if len(line)>0:
            words=line.split(' ')
            for word in words:
                if (len(array[j])+len(word)) <= w:
                    array[j]+=word+' '
                else:
                    array.append('')
                    j += 1
                    array[j]+=word+' '
        else:
            array.append('\n')                   # new line
            j += 1
    return array
           

""" function to write formatted string to a new file 'output' """
def write(filename, lines):
    f = open(filename, 'w')
    for line in lines:
        print(line,file=f)
    f.close()

""" main function that takes in information/input"""
def main():
    filename=input('Enter the input filename:\n')
    output=input('Enter the output filename:\n')
    width=eval(input('Enter the line width:\n'))
    lines = read(filename)
    lines = reformat(lines,width)
    #for i in lines:
        #print(i)
    write(output,lines)

main()