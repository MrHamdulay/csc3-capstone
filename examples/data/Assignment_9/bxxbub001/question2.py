filename = input("Enter the input filename:\n") #input("Enter the marks filename:\n")
outputName = input("Enter the output filename:\n")
num = eval(input("Enter the line width:\n"))
g = open(filename, "r")
lines = g.readlines()
g.close()
newStr = ""
#num = 40
def removeN(s):
    return s[:-1]
def para(s,n):
    flag = 0
    if s == "":
        return s
    elif len(s)<n:
        return s + " "
    else:
        for x in range(len(s[:n]),0,-1):
            if s[x]==" ":
                flag =-1
                return s[:x]+"\n"+para(s[x+1:],n)
            elif flag == -1:
                break
            
            
            else:
                continue
            
            
                
        #return s[:n]+"\n"+para(s[n:],n)
g= open(outputName, "w")
for x in range(len(lines)):
    line = lines[x]
    if lines[x][len(lines[x])-1:]=="\n":
        line = removeN(line)
    print(para(line,num),file=g,end="")
    #print("\n",file=f,end="")
g.close()    
   
  