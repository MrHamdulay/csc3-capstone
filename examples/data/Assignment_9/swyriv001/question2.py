"""program to reformat a text file
   Rivoningo Seweya
   14 May 2014"""
inputname=input("Enter the input filename:\n")
outputname=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))
#open the input file
f=open(inputname,"r")
#open the ouput file
outfile=open(outputname,"w")
file=f.readlines()#read the lines
f.close
x=-1  #keep the counter of the length  
for i in file:
        if file!="\n":
                b=i.replace("\n"," ")#replace \n
                line=(b.split(" "))
                for j in line:  #keep counter
                        x+=len(j)+1
                        if x<=width:
                                print(j,file=outfile,end=" ")
                        else:   
                                print(file=outfile) #print the new setence in the file in a new line
                                print(j,file=outfile,end=" ")
                                x=len(j)
        else:
                line=i# make i=line
                print(file=outfle)
                print(file=outfile)
                x=-1
outfile.close()