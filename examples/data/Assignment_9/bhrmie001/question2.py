def formatted(string, width):
    listed_strings=[]
    fmat="{0:"+width+"}"
    num=eval(width)
    if len(string)<eval(width):
        if string=="":
            return listed_strings
        else:
            listed_strings.append(fmat.format(string[:]))
            return listed_strings
    elif len(string)> eval(width):
        num=eval(width)
        char=string[num]
        if char==" " or char=="." or char=="\n":
            listed_strings.append(fmat.format(string[:num]))
            return formatted(string[num+1:], width) + listed_strings
        if string[num]!=" " or string[num]!="." or char!="\n":
            while not (char==" " or char=="." or char=="\n"):
                if len(string)>1:
                    num-=1
                    char=string[num]
            listed_strings.append(fmat.format(string[:num]))
            return formatted(string[num+1:], width) + listed_strings
    return listed_strings

def main():
    filer=input("Enter the input file name:\n")
    f=open(filer, "r")
    whole=f.read()
    f.close()
    z=""
    for i in [whole]:
        for j in i:
            if j!="\n":
                z+=j
            elif j=="\n":
                z+=" "
    filew=input("Enter the output file name:\n")
    width=input("Enter the line width:\n")
    listed_string=formatted(z, width)
    y=open(filew, "w")
    for i in range(1, len(listed_string)):
        print(listed_string[-i], file=y)
    print(listed_string[0], file=y)
    y.close()
    
main()    