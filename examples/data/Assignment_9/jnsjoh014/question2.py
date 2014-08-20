__author__ = 'JNSJOH014'
"""Question 2, Assignment 9
15/05/2014"""

def wrap():
    #inputs
    in_name = input("Enter the input filename:\n")
    out_name = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    #Write file to a long string
    f = open(in_name,"r")
    long_string = f.read()
    f.close()
    #remove \n except for new paragraph
    long_string.replace("\n\n","qwerty01")#<<<random string that won't be in text
    long_string.replace("\n"," ")
    long_string.replace("qwerty01","\n\n")

    lines=[]
    counter=0#line counter
    addword=""#temporary storage of a the modified content of the file
    while len(long_string)>0 or addword!="":#while data left or
        lines.append(addword)
        addword=""
        while  1:
            if len(long_string)==0:
                break
            elif long_string.find(" ")!=-1:#found a space, therefore new word
                addword = long_string[0:(long_string.find(" ")+1)]
                long_string = long_string[long_string.find(" ")+1:]#remove word from long string
            else:
                addword = long_string
                long_string = ""

            end = len(addword)
            if addword[-1]==" ":
                end-=1

            if "\n\n" in addword:#split addword into two lines
                line1 = addword[0:addword.find("\n\n")]
                lines[counter]+=line1
                counter+=2
                lines.append("")
                line2 = addword[addword.find("\n\n")+2:]
                lines.append(line2)
            elif (len(lines[counter])+end)<=width:
                lines[counter]+=addword
                addword=""
            else:
                break
        counter+=1#increment line no

#print to output file
    f = open(out_name,'w')
    for line in lines:
        print(line,file=f)
    f.close


if __name__=="__main__":wrap()