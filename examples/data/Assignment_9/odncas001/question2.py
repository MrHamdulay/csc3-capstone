"""paragraph editor for given text files
casey o'donnell
12 may 2014"""

inp_filename=input("Enter the input filename:\n")
out_filename=input("Enter the output filename:\n")
linewidth=eval(input("Enter the line width:\n"))

def line_format(s,x):
    line=""
    if len(s)<x:
        print(s,file=f)
    else:
        for i in range(linewidth,0,-1):
            if s[i]==" ":
                line=s[:i]
                print(line,file=f)
                break
        line_format(s[i+1:],x) 
        
               
f=open(inp_filename,"r")
filestring=f.read()
f.close()

paragraphs=filestring.split("\n\n")
final_paragraphs=[]
for string in paragraphs:
    final_paragraphs.append(string.replace("\n"," "))

f=open(out_filename,"w")
for paragraph in final_paragraphs:
    line_format(paragraph,linewidth)
    print(file=f)
f.close()
