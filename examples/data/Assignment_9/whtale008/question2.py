""" program to format a txt file
alexander whiting
14 may 2014"""

def lines(para,length,filename):
    i = 0
    pos1 = 0
    for sent in para:
        
        while len(sent)>0:
            if len(sent)< length:
                print(sent,file = filename)
                break
            elif i == length:
                if sent[i] == ' ':
                    pos1 = i
                    print(sent[0:pos1],file = filename)
                    sent =""+ sent[pos1+1:]
                else:
                    print(sent[0:pos1],file = filename)
                    sent =""+ sent[pos1+1:]                
                i = 0
                pos1= 0        
            elif sent[i] == " ":
                pos1 = i
                i+=1
                    
           
            else:
                i+=1
    
 
infile = input("Enter the input filename:\n")   
outfile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

f = open(infile,"r")
data = f.readlines()
f.close
sent = ''
para = []
i = 0
while i <len(data):
    if data[i] == '\n':
        sent += "\n"
        para.append(sent)
        sent=''
        sent = data[i+1].rstrip('\n')
        i = i+1
        
    elif i>=1:
        sent += " "+ data[i].rstrip("\n")
    else:
        sent += data[i].rstrip("\n")
    i += 1
para.append(sent)
f = open(outfile, "w")
lines(para,width,f)
f.close()    