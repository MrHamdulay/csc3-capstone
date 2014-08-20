import textwrap
def mean(file,file1,wid):
    f = open(file,"r")
    allLines = " ".join(f.readlines()).replace("\n "," ")
    
    allLines = textwrap.wrap(allLines, width=wid, break_long_words=False)
    
    
    f.close()
    
    g = open(file1,"w")
    for i in allLines:
        i=i+'\n'
        g.write(i)
        
def main():
    x = input('Enter the input filename:\n')
    y = input('Enter the output filename:\n')
    w = eval(input('Enter the line width:\n'))
    mean(x,y,w)
main()
             
    