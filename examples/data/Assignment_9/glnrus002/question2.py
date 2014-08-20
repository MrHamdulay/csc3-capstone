#GLNRUS002
#ASSIGNMENT 9
#QUESTION 2

def par(t,w):#text,width
    words=t.split(" ")#individual words
    op=""#used to accumulate new string
    tmp=0#used to keep track of letters per line
    
    for i in words:#while there are still words left
        if tmp+len(i)<w:#length of single line thus far
            op=op+i+" "#adds word and a space to current string
            tmp+=len(i)+1#adds total of wordlength and 1 for space char to total of line
        else:#word too long
            op=op+"\n"+i+" "#adds next line char plus word plus emptu space for next line
            tmp=len(i)+1#resets char count for new line, adding the current contents of the new line     
    return op

def store_string_in_file(value,fyle):#finally stores string into file
    g=open(fyle,"w")
    print(value,file=g)
    g.close()  #initial storage of file with spaces at the end
    
    l=open(fyle,"r")#for later reading
    lines=l.readlines()
    l.close
    
    k=open(fyle,"w")
    for i in lines:#remove trailing spaces
        print(i[:-2]+" ",file=k)
    k.close()
    
if __name__ == "__main__":
    infile=input("Enter the input filename:\n")
    outfile=input("Enter the output filename:\n")
    width=eval(input("Enter the line width:\n"))
######################input file interaction########
    f=open(infile,"r")
    lines=f.readlines()
    f.close()
###########remove trailers###########################   
    c=0
    for i in lines:#removes\n
        lines[c]=i[:-1]+" "
        c+=1
#########convert list into a single string######################       
    alltext=""
    c=0
    for j in lines:
        alltext=alltext+lines[c]
        c+=1
##########operations###############################  
    store=par(alltext,width)
    store_string_in_file(store,outfile)