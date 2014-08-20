""" program to reformat a text file so that all lines are at most a given length
tafara mtutu
11 may 2014"""

temp = ""
infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

f = open (infile, "r")
text = f.read()
f.close()

f = open(outfile, "w")
#h = f.read()
f.close()

for i in range(len(text)):
    g = text.find("\n\n")
    if g != -1 :
        text = text[:g] +"00"+ text[g+2:]

for i in range(len(text)):
    q = text.find("\n")
    if q != -1 :
        text = text[:q] +" "+ text[q+1:]
        
for i in range(len(text)):
    g = text.find("00")
    if g != -1 :
        text = text[:g] +"\n\n"+ text[g+2:]
              
for i in range(len(text)):
    if text[i] == '\n':
        f = open (outfile, "a")
        print(temp, file = f)
        f.close() 
        temp = ""
        continue
    elif len(temp) != width:
        temp += text[i]
    elif len(temp) == width:
        if text[i] == " ":
            f = open (outfile, "a")
            print(temp + text[i], file = f)
            f.close()  
            temp = ""
        else:
            for j in range(len(temp)-1,0,-1):
                if temp[j] == " ":
                    break 
            f = open (outfile, "a")
            print(temp[:j+1], file = f)
            f.close()  
            temp = temp[j+1:]+text[i]
f = open (outfile, "a")
print(temp, file = f)
f.close()  

        
                                               