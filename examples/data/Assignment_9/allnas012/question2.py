infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
w = eval(input("Enter the line width:\n"))

input_file=open(infile,"r")         
output_file=open(outfile,"w")       

                                    
lines = input_file.readlines()        
input_file.close()                   
c=-1                             
for line in lines:
   if line!='\n' :
       line=line.replace('\n','')   
       line=line.split(' ')         
       for i in line:
           c+=len(i)+1      
           if c <= w:
               print(i,file=output_file,end=' ')
           else:
               print(file=output_file)
               print(i,file=output_file,end=' ')
               c=len(i)
   else:
       line=line                    
       print(file=output_file) 
       print(file=output_file)
       c=-1
output_file.close()



















'''infile=input("Enter the input filename:\n")
outfile=input("Enter the output filename:\n")
w=eval(input("Enter the line width:\n"))

input_file=open(infile,"r")
output_file=open(oufile,"w")

line=input_file.readlines()
input_file.close()

x=-1
for i in line:
    if i!="\n":
        i=i.replace("\n","")
        i=i.split(" ")
        for word in i:
            c+=len(word)+1
            if c<=w:
                print(word,f=output_file,end=" ")
            else:
                print(f=output_file)
                print(word,f=output_file,end=" ")
                c=len(word)
    else:
        i=i
        print(f=output_file)
        print(f=output_file)
        c=-1
output_file.close()'''
            
        
