'''Wade Cresswell
Question2'''
print('Enter the input filename:')
filename = input()
print('Enter the output filename:')
ofile = input()
print('Enter the line width:')
width = eval(input())+1
inf = open(ofile, "r") 
fileinstring = inf.read() #opens and reads reader file into a string  
inf.close()
def formatfun(para,widthf): #function to reformat the string to desired length
    user = para[:widthf] #will only go as long as required
    stringlength = len(para) 
    if stringlength > widthf: #if the string is longer than desired width
        if(para[:widthf + 1] == " "): #if string empty
            writefile.write(user + "\n")
            formatfun(para[widthf:],widthf) #recursion
        else:
            charl = user[::-1]
            space = charl.find(" ")
            z = charl[space:]
            y = charl[:space]
            writef.write(z[::-1] + "\n")
            formatfun(y[::-1] + para[widthf:],widthf) #recursion
    else:
        writef.write(para + "\n\n") #if not longer than desired width, no reformatting necessary
        
writef = open(filename, "w")
if "\n\n" in fileinstring:
    fileinstring = fileinstring.replace("\n", " ")
    splitpara = fileinstring.split("  ")
    for x in splitpara:
        formatfun(x,width)
else:
    fileinstring = fileinstring.replace("\n"," ")
    formatfun(fileinstring,width) 
writef.close()