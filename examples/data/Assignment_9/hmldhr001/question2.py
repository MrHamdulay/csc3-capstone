
#Dhriven Hamlall

def main():
    InputFile=input("Enter the input filename:\n")
    outputFile=input("Enter the output filename:\n")
    w=eval(input("Enter the line width:\n"))
 #===============================================================================   
    word=""
    flag=False    
    printline=""
    c=0 #counter
    
#==================================================================================
    f= open(InputFile,"r")
    for line in f:

        printline+= line+ " "
    printline1=f.read()
    f.close()
    
#======================================================================================
    printline=printline.replace("\n","X") #removing new line char
    lines=printline.split(" ")
    f=open(outputFile,"w")
#======================================================================================================  

    while c<len(lines):
        printOut=""
        l=0 #length
        
        while c!=len(lines)and (l+(len(lines[c])))<=w:
            try:
                if (c+1)!=len(lines) and (lines[c])[-1]=="X" and lines[c+1]=="X":
                    
                    printOut=printOut + lines[c]+" "
                    printOut=printOut.replace("X","")
                    l=printOut #l - length
                    c=c+2
                    flag=True
                    break
                
            except IndexError:
                pass
            printOut= printOut + lines[c]+" "
            printOut=printOut.replace("X","")
            l=len(printOut)
            print(printOut)
            c+=1
        print(printOut,file=f)
        if  flag:
            print("",file=f)
            flag=False
        
    f.close()
    
main()
        
    