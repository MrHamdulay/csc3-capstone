#let's try this again, shall we?
#victor gueorguiev
#14 may 2014

def main():
    ifile = input('Enter the input filename:\n')
    ofile = input('Enter the output filename:\n')
    column_width = eval(input('Enter the line width:\n'))
    f = open(ifile,"r")
    lines = f.readlines()
    f.close()
    long_string = ''
    result = ''
    for line in lines:
        if line == '\n':
            long_string += line
        else:
            long_string += line[:-1] + ' '
    while long_string != '':
        temp  = long_string[:column_width+1]
        if temp.find('\n') != -1:
            temp = temp[:temp.find('\n')+1]
            #print(temp)
            result += temp + '\n'
            long_string = long_string.replace(temp,'')
        elif temp.find(' ') != -1:
            while temp[-1] != ' ':
                temp = temp[:-1]
            #print(temp)
            result += temp + '\n'
            long_string = long_string.replace(temp,'')
        else:
            #print(temp)
            result += temp
            long_string = long_string.replace(temp,'')
    f = open(ofile,"w")
    print(result,file=f)
    f.close()

main()   