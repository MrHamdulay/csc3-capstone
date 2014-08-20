import question1
def main():
    inputFilename=input("Enter the input filename:\n")
    arrcontent=question1.getFileContent(inputFilename)
    outputFilename=input("Enter the output filename:\n")
    width=int(input("Enter the line width:\n"))
    formatFile(arrcontent,outputFilename,width)
def formatFile(arrcontent,filename,width):
    f=open(filename,'w')
    linep=""
    for i in range(len(arrcontent)):
        line=arrcontent[i].split(" ")
        for j in line:
            if chr(10) in j:
                j=j.replace(chr(10),'')
                j=j.replace(' ',"")
            wordlen=len(j)
            if (wordlen+len(linep))<=width:
                print(j," ",end="",file=f,sep="")
                linep=linep+j+" "
            else:
                print("\n",j," ",sep="",end="",file=f)
                linep=j+" "
    f.close()
if __name__=='__main__':
    main()