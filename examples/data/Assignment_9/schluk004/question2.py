#Program to format text files
#Luke Schwartzkopff
#13 May 2014

inname=input("Enter the input filename:\n")
outname=input("Enter the output filename:\n")
lwidth=eval(input("Enter the line width:\n"))

f = open (inname, "r") #open file and count lines
lcount = 0
for line in f:
    lcount += 1
f.close ()

fstring=""
f=open(inname,"r") #open file and add each line into one string, add a space for lines but remove endline char
for i in range(lcount):
    fstring+=f.readline().strip("\n")+" "
f.close()

rev=0
flag=0
olist=[]

for i in range(len(fstring)): 
    if i==flag+lwidth-1:
        if fstring[i]!=" " and fstring[i+1]==" ": #check to see whether the break point falls on a space
            olist.append(fstring[flag:i+1]) #append all up to this point to a list
            flag=i+1 #set point for continuation
        else: #if the break point falls on a word case
            rev=i
            while(fstring[rev]!=" "): #loop back to the space
                rev=rev-1
            olist.append(fstring[flag:rev]) #append to list
            flag=rev+1
    elif i==len(fstring)-1: #case for last formatted line where it may not reach the specified limit (not enough chars remaining)
        olist.append(fstring[flag:len(fstring)])
          
f=open(outname,"w")  #writing to text file

for i in range(len(olist)):
    if olist[i][0]==" ":
        olist[i]=olist[i][1:]
    
    
for i in olist:
    print(i,file=f)
    
f.close()