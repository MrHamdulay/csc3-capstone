"""reformat text so all lines are less than a certain length
Haaroon Cassiem
11 May 2014"""
def loadFile(f):
    #load file data into a list
    l=open(f,"r")
    words=[]
    
    for line in l:
        if len(line)!=1:
            for wrd in (line[:-1].split(" ")):
                
                words.append(wrd)
        else:
            words.append(line)
    
    return words

def writeFile(d,o,w):
    #write file data from list to new file
    l=0
    output=open(o,"w")
    for i in range(len(d)):     
        
        q=len(d[i])        
          
        if(d[i]=="\n"):
            print(d[i],file=output)
            l=0        
        elif(l==0):           
            print(d[i],sep="",end="",file=output)
            l+=q
            
        elif(0<l+q+1<=w):                       
            print(" ",d[i],sep="",end="",file=output)
            l+=q+1            
        elif(l+q+1>w):                       
            print("\n",d[i],sep="",end="",file=output)
            l=0+q
            
if __name__=="__main__":
    f=input("Enter the input filename:\n")
    d=loadFile(f)
    o=input("Enter the output filename:\n")
    w=eval(input("Enter the line width:\n"))
    writeFile(d,o,w)