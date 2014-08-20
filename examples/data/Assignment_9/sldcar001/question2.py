def width():
    infilename=input("Enter the input filename:\n")
    outfilename=input("Enter the output filename:\n")
    width=eval(input("Enter the line width:\n"))    
    inf=open(infilename,"r") 
    outf=open(outfilename,"w")
    count=0
    just=0
    for i in  inf.readlines():
        if i=='\n':
            outf.write('\n\n')
            count=0
            just=0
        else:
            inff=i.replace('\n','').split(' ')
            for word in inff:
                count+=len(word)
                if count+1<=width:
                    if just==0:
                        outf.write(word)
                        just=1
                    else:
                        outf.write(' '+word)
                        count+=1
                    
                else:
                    outf.write('\n'+word)
                    count=len(word)

    inf.close()
    outf.close()
    outf=open(outfilename,'r')
    print(outf.read())
        
width()
        