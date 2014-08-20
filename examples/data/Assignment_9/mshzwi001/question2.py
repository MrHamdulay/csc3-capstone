# a Python program to to reformat a text file so that all lines are at most a given length
# mashau zwivhuya
# 12 may 2014
#getting input
file=input("Enter the input filename:\n")
out=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))
#opening file
f=open(file,"r")
lines=f.readlines()
f.close()
#creating output file
g=open(out,"w")
words=[]
words2=[]
for i in lines:
    for j in i:
        words.append(j)
#removing "\n"

for i in words:
    if i=="\n":
        x=words.index(i)
        del words[x]
        words.insert(x," ")
#putting paragraphs together after removing \n       
words="".join(words)
words=words.split(" ")
for i in words:
    words2.append(i+" ")
x=words2[-1]
x=x[:-1]
del words2[-1]
words2.append(x)

#--------------------------------------------------------------
#creating a new list of words with spaces
spaceless=[]
for i in words:
    if i=="":
        continue
    else:
        spaceless.append(i)
spacefull=[]
for i in spaceless:
    spacefull.append(i+" ")

#--------------------------------------------------------------------------
#counting number of words
count=0
for i in spacefull:
    hei=len(i)
    count+=hei
range1=1+(count//width)
#--------------------------------------------------------------------------
#manipulation of words anl looping through all words
x=0
main1=[]

for i in range(range1):
    length=0
    for i in spacefull[x:]:
        lengthy=len(i)
        length+=lengthy
        if length<(width+1):
            main1.append(i)
            #print(length,"length")
        else:
            length=0
            main1.append("\n")
            x=spacefull.index(i)
            #print("----------------------------------------------------",x)
            break
        


#--------------------------------------------------------------------------
# printing out to new file
for i in main1:
    print(i,end="",file=g)
g.close()
    
    
#for i in main1:
#    print(i,end="")