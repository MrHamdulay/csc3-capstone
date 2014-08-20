'''program to reformat a text file so that all lines are at most a given length. Do not break up words. 
Daniel M.Tamale
TMLDAN001
2014-05-16'''

file_input = input("Enter the input filename:\n")
f = open (file_input, "r")
l = f.read() 
f.close ()
file_output = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
f = open(file_output,"w")
para_words = l.split(" ") 

c = 0
for i in range(0,len(para_words)):
    if c+len(para_words[i])<=width: 
        print(para_words[i]," ",sep="",end="",file=f) 
        c+=len(para_words[i])+1 
    else:
        print("\n",para_words[i]," ",sep="",end="",file=f)
        c = len(para_words[i])+1
f.close() 