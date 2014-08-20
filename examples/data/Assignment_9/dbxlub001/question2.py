""" paragraph fixer
Lublethu Dube
may 13 2014"""
def forty():
    
    #get txt as a string then put every word as an array
    file1=input("Enter the input filename:\n")
    f=open(file1,"r")
    lines=f.read()
    f.close()
    newlines=lines.split(" ")
    
    
    #get width to be used and save it under a variable count
    file2=input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    mainMan1=[]
    for i in newlines:
        if "\n\n" in i:
            j=i.split("\n\n")
            mainMan1.append(j[0])
            mainMan1.append("\n\n"+ j[1])
        elif "\n" in i:
            j=i.split("\n")
            mainMan1.append(j[0])
            mainMan1.append(j[1])
        else:
            mainMan1.append(i)
    
            
            

    mainMan=[]
    count=width
    
   
    for i in mainMan1:
        num=len(i)+1
        
        #remove paragraphs n make them pretty
        if ("\n\n") in i:
            mainMan.append("\n\n")
            i=i[2:]
            width=count
               
            
        #put each word into a list and insert a new line when maximum number of chararters has bee reached    
        if width==count:
            mainMan.append(i)
            width-=len(i)
            
        elif num<=width:
            mainMan.append(" ")
            mainMan.append(i)
            width-=num

        else:
            mainMan.append("\n")
            width=count
            mainMan.append(i)
            width-=len(i)
            
    #make it a string then put into new file
    realDeal="".join(mainMan)
    
    f2=open(file2,"w")
    print(realDeal,file=f2)
    f2.close()
            
forty()