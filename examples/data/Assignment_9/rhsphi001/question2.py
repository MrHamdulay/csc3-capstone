'''Phillip Ruhesi
15/05/2014
program to format text'''



fname=input('Enter the input filename:\n')
infile=open(fname,'r')
data=infile.readlines()
infile.close()
fout=input('Enter the output filename:\n')
outfile=open(fout,"w")

para=[[]]
#Splits every line in input file into words and adds them to the paragraph
for lin in data:
    lin = lin.replace("\n","").split(" ")
    if lin == ['']:
        para.append([])    
    else:
        para[-1] += lin
         
width=eval(input('Enter the line width:\n'))


for paragraph in para:
    position=1
    line=paragraph[0]
    while position<len(paragraph):
        if len(line + ' ' + paragraph[position])<=width:  #checks if the length of the current string plus a space plus the next word is less than width
            if line == '':
                line += paragraph[position]               #adds the next word plus a space to the string
            else:
                line+=' '+paragraph[position]                       
            position+=1
        else:
            outfile.write(line+'\n')                      #writes the last line and new line character to the file
            line=''
    outfile.write(line+'\n\n')                            #puts spaces between paragraphs
outfile.close()            
        