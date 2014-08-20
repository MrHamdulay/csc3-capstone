def paragraphs(f_in,f_out,w):
    w=eval(w)
    empt=""
    length = 0
    rem= w
    f=open(f_in,"r")
    f=f.read()
    f=f.split("\n")
    f=" ".join(f)
    f=f.split(" ")
    
    for i in f:                
        if len(i) <= rem:
            empt=empt + i + " "
            rem= rem - (len(i) + 1)
        else:
            if len(i) > rem:
                empt=empt + "\n" + i + " "
            rem=w - (len(i) + 1)
            
    f2=open(f_out,"w")
    f2.write(str(empt))
    f2.close()
    
    
paragraphs(f_in=input("Enter the input filename:\n"),f_out=input("Enter the output filename:\n"),w=input("Enter the line width:\n"))