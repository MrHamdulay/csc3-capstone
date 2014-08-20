'''program to put sentences in a specified width
matshepo mashabela
14 may 2014'''

#sp=space_indices

inp=input("Enter the input filename:\n")
f=open(inp,"r")
lines=f.read()
f.close()

out=input("Enter the output filename:\n")
width=eval(input("Enter the width:\n"))

fi=open(out,"w")
def paras(lines):
     sp=[]
     length=len(lines)
     sliced=lines[:width]
     if length > 0:
          if length > width:
               if "space" in sliced:
                    position=sliced.find("space")
                    upto=position+len("space")
                    print(sliced[:upto], file=fi)
                    #print("", file=fi)
                    return paras(lines[upto+1:])
               
               elif "algorithm" in sliced:
                    position=sliced.find("algorithm")
                    upto=position+len("algorithm")
                    print(sliced[:upto], file=fi)
                    #print("", file=fi)
                    return paras(lines[upto+1:])
               
               elif "storage" in sliced:
                    position=sliced.find("storage")
                    upto=posotion+len("storage")
                    print(sliced[:upto],file=fi)
                    #print("", file=fi)
                    return paras(lines[upto+1:])
     
               else:
     
                    for i in range(width):
                         if sliced[i]==" ":
                              sp.append(i)
                    maximum=max(sp) 
                    print(lines[:maximum], file=fi)     
                    return paras(lines[maximum+1:])
          elif length<=width:
               print(lines, file=fi)
               fi.close()
paras(lines)      




