"""Tevin Chetty
14 May 2014
Program to find the standard deviation and average if a list of marks"""
i=input("Enter the input filename:\n")
ed=open(i, "r")
ln=ed.read()
ed.close()
t=ln.split("\n\n")
text=""
for txt in t:
    text=text+txt.replace('\n',' ')
print(text)
file_output=input("Enter the output filename:\n")
width=eval(input("Enter the line width: \n"))
no_lines=(len(text)//width)+1
product=open(file_output, "w")
count=0
print(no_lines)
while count<=no_lines:
    if len(text)<=width:
        print(text, file=product)
        break  
    elif text[:width]==" " :
        print(text[:width], file=product)
        text=text[width:]
        count+=1
    else:
        check=text[:width]
        for i in range (len(check),-1,-1):
            if text[i] == " " :
                print(text[:i], file=product)
                text=text[i+1:]
                count+=1
                break
                
product.close()