"""Program to reformat a text file to given length per line
Carla Wilby
10 May 2014"""

infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

file = open(infile, "r") #Opening file to read
f = file.read()
file.close()
count = 0
origpos = 0

newfile = open(outfile, "w") #Opening file to write to
#print(f)
cnt = 0
while cnt < (len(f)):
    #print("here1",f[cnt:cnt+1])
    if f[cnt:cnt+1] == '\n':
        if f[cnt+1:cnt+2] == '\n':
            cnt+=2
        #print(f[:cnt])
        #print("split")
        #print(f[cnt+1:])
        else:
            f = f[:cnt]+" "+f[cnt+1:]
            cnt+=1
    else:
        cnt+=1    
        
#print(f)

def counter(count,origpos):
    count += width #Next number of specified characters
    if count <= len(f):
        while f[count] != " ": #Finding closest space character less than the width
            count-= 1
        else:
            print(f[origpos:count], file=newfile) #Printing each line to the output file
            origpos = count + 1
            counter(count,origpos)
    else:
        print(f[origpos:], file=newfile) #Printing the remaining line to the output file
    newfile.close()
        



if __name__ == '__main__':     
    counter(count,origpos)        

