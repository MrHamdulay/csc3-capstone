"""program to created formatted paragraph
FRDYON001
13 May 2014"""

# get input file, create output file and get width of paragraph that must be creeated
inputfile=input("Enter the input filename:\n")
outputfile=input("Enter the output filename\n")
width=eval(input ("Enter the width:\n"))

infile=open(inputfile,"r")
outfile=open(outputfile,"w")
#make a list of all the lines
alist=[]
for i in infile.readlines():
        #x=i[:-1]
        if i=="\n":
                alist.append(i)
        #remove spaces at the end of newline
        elif (i[-1]=="\n"):
                        x=i[:-1]        
        
                        alist.append(x)

#from the list of lines make a list of indiviual words and spaces for where there are double spaces
new_list=[]

for i in alist:
        if i=="\n":
                new_list.append(i)
        elif i!=" ":
                
                x=i.split(' ')
                new_list+=x
        else:
                new_list.append(i)


#begin making lines to put into new file and keep track of the length
track=""

for k in range (len(new_list)):
        #check if new word that must be added plus what already exists is less than or equal to the width
        stopper=len(new_list[k])+len(track)
        if stopper<=width:
                
                if new_list[k]=="\n":
                        print(track[:-1],file=outfile)
                        track=(" "*width)      
                else:
                        track+=new_list[k]+" "
        else:
                #if greater than the width then go to new line and initialise the length of that line to 0 again
                print(track[:-1],file=outfile)    
                track=""
                track+=new_list[k]+" "
#print out the last line
print(track[:-1],file=outfile)   

#close both files   
infile.close()
outfile.close()

