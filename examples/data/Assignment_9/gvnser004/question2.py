

lines=[]
flines=[]
inp_file= input("Enter the input filename:\n")
out_file= input("Enter the output filename:\n")
leng=eval(input("Enter the line width:\n"))
rem=""
file=open(inp_file,"r")
count=0

for line in file:
    rem=line
    while len(rem)>leng:
        k=rem[0:leng]
        s=k.rfind(" ")
        
        lines.append(rem[0:s])
        rem=rem[s:len(rem)]

lines.append(rem) 



file.close()
    

outfile=open(out_file,"w")

for i in range(len(lines)):
    if(lines[i][0]==" "):
        lines[i]=lines[i][1:]
    print(lines[i], file=outfile)


outfile.close()


    