'''Program to reformat a textfile
Matshepo Malatji
14 May 2014'''

#Get input from user 
input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
#print(width)

#define format string
sObj = "{0:<" + str(width) + "}"

#open the file and insert it into a string variable
s = ''
in_f = open(input_file,"r")
for line in in_f:
    if line[-1] == '\n':
        s += line[:-1]
    else:
        s += line
        
in_f.close()


while s != '':
    if len(s) >= width:
        #shorten the string
        if s[width] == ' ':
            newline = s[:width+1]
        else:
            pos = width
            while not s[pos] == ' ':
                pos -= 1
            newline = s[:pos+1]
    else:
        newline = s
        
    out_f = open(output_file,"w")
    print(sObj.format(newline), file = out_f)
    out_f.close()
    
    s = s[len(newline):]