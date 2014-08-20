from textwrap import *

infile=input("Enter the input filename:\n")

outfile=input("Enter the output filename:\n")

#w=input("Enter the line width:\n")
w=40


#read from file input.txt

f=open(infile,"r")
sent=f.read()
#listc=[]
#for l in lines:
    #listc.append(l)

f.close



#Remove the newline char from end of lines






#separate words in list by width given


width=w
dedented_text = dedent(sent).strip()

     

new=fill(dedented_text, width=width)

g=open(outfile,"w")
print(new, file=g)
g.close






#Write to output file, one line at a time using created array.
#newfile=open(infile,"w")



#print(new,file=infile,end="")

 #       print("{0:<w}".format(sentence[i],file=outfile))
#newfile.close()
        
        
    
    
