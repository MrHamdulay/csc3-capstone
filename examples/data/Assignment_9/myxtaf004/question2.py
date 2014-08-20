""""Breaks up sentences in a file into paragraphs
Tafadzwa Moyo
12 May 2014"""

#input
i_name=input("Enter the input filename:\n")
o_name=input("Enter the output filename:\n")
n=eval(input("Enter the line width:\n"))
#get file
fi=open(i_name, "r")
lines=fi.readlines()
fi.close()
string=['']
#Turns the lines list into a string of values
for i in lines:
    if i!="\n":
        if i.find("\n")>-1:
            string[-1]+=i[:-1]+" "
        else:
            string[-1]+=i
    else:
        string.append("")
#writes manilapulated string into output file
for w in range(len(string)-1):
    for o in range(len(string[w])-1):
        if string[w][o]==" ":
            if string[w][o+1]==" ":
                string[w]=string[w][:o]+string[w][o+1:]
output=[]
x=0
l=string

for r in range(len(string)):
    output.append('')
    while len(string[r])>=n:
        string.append('')
        x=string[r][:n].rfind(" ")
        if x>-1:
            output[-1]+=string[r][:x]+"\n"
            string[r]=string[r][x+1:]
    output[-1]+=string[r][:]
fo=open(o_name, "w")
for i in output:
    print(i, file=fo)
    print(file=fo)
fo.close()