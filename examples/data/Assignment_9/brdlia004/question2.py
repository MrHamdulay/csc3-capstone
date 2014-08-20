"""File reformatter"""
#Liam Brodie
#BRDLIA004
#11 May 2014

print("Enter the input filename:")
infile = input("")
file = open(infile,"r")
string = file.readlines()
file.close()

print("Enter the output filename:")
outfile = input("")

linelength = eval(input("Enter line width:\n"))


newS = ""
for line in string:
    if line[-1] == "\n":
        newS += line[:len(line)-1]
    else:
        newS += line
        
print(newS)



def newline(newS):
    
    if(len(newS)==0):
        return ""
    else:
        if(newS[:2]!='\n'):
            Space = newS[:linelength].rfind(" ")
            if(Space>0):
                #print(Space*" ")
                #print(newS[:Space+1])
                return newS[:Space] + "\n" + str(newline(newS[Space+1:]))
        else:
        
            return newline(newS[2:])
        
output = open(outfile,"w")
outtext = newline(newS)
output.write(newS)       
output.close()