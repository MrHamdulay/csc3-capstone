#ASSIGNMENT 9
#QUESTION 2
#NLTWES001

fname=input("Enter the input filename:\n")
f=open(fname,"r")
text=''
for line in f:
    try:
        text+=line[:-1]+" "
    except:
        text+=line[:-1] 
text.replace("\n","")
f.close()
f=open(fname, "r")
for line in f:
    last=line
              
text = text[:-1] + last[-1:]
                
print(text)

f.close()