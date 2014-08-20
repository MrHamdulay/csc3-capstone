i_file=input("Enter the input filename:\n")
o_file=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

read=open(i_file,"r")
lines=read.readlines()
write=open(i_file,"w")
for i in lines:
    i=i[:-1]+" "        #chopping off newline character and adding a space
write.close()

read2=open(i_file,"r")
read_all=read2.read()
write2=open(i_file,"w")
for i in read_all:
    if read_all[width]==" ":
        i=i[1:]+"\n"
    else:
        pos=read_all[:i].rfind(" ")
        read_all[pos]=read_all[1:]+"\n"
    print(i,file=o_file)
write2.close()

        

        
    