def redo():
    filename_in=input("Enter the input file:\n")
    filename_out=input("Enter the output file:\n")
    width=eval(input("Enter the line width:\n"))
    #opening and viewing data
    f=open(filename_in,"r")
    lines=f.readlines()
    f.close
    #get words for length of line
    line=""
    count=0
    for i in lines:
        line += i
    line = line.split()
    count=0
    new_doc=""
    for j in range(len(line)):
        if count< width and (count+len(line[j])<width):
            new_doc+= line[j]+" "
            count+= len(line[j])+ 1
        elif count+len(line[j])>width:
            new_doc+="\n"+ line[j]+" "
            count=len(line[j])+1
            
        elif count+len(line[j])==width:
            new_doc+=line[j]+"\n"
            count=0
        
            

    g = open(filename_out,"w")
    filename_out = print(new_doc, file = g)
    g.close()
                    
                                
                   
redo()                   
                   