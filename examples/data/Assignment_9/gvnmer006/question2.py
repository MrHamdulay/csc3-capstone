#Program to reformat a text file so that the lines are a given length
#GVNMER006-Merosha Govender
#15 May 2014

    
def main():
    fName=input("Enter the input filename:\n")
    oName=input("Enter the output filename:\n")
    fWidth=eval(input("Enter the line width:\n"))
    #fName="input.txt"
    #oName="output.txt"
    #fWidth=40
    printline=""
    count=0
    f= open(fName,"r")
    word=""
    True_False=False
    for line in f:
       # length=0
       # printLine=""
       # count=0
       # line1=line.split(" ")
       # while (len(printLine)+len(line1[count]))+1<=fWidth:
       #     printLine+=line1[count]+" "
       #     count+=1
       # print(printLine)
       # for i in range(count,(len(line1))):
       #         line1[i-count]=line1[i]
        printline+= line+ " "
    printline1=f.read()
    
    
    f.close()
    printline=printline.replace("\n","X")
    #printline=printline.replace("X","\n\n")
    #printline=printline.replace("\n"," ")
    #printline=printline.replace("  "," ")
    
    lines=printline.split(" ")
    f=open(oName,"w")
    
    while count<len(lines):
        length=0 
        lineprint=""
        while count!=len(lines)and (length+(len(lines[count])))<=fWidth:
            try:
                if (count+1)!=len(lines) and (lines[count])[-1]=="X" and lines[count+1]=="X":
                    #length+=len(lines[count])
                    lineprint+= lines[count]+" "
                    lineprint=lineprint.replace("X","")
                    length=lineprint
                    count+=2
                    #length+=1
                    True_False=True
                    break
            except IndexError:
                pass
            lineprint+= lines[count]+" "
            lineprint=lineprint.replace("X","")
            length=len(lineprint)
            print(lineprint)
            count+=1
        print(lineprint,file=f)
        if  True_False:
            print("",file=f)
            True_False=False
        
    f.close()
        


main()
        
    
