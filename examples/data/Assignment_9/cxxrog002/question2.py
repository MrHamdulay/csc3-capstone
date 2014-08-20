"""change text to equal a correct format
Roger Cox
14 May 2014"""


text_im=input("Enter the input filename:\n")
f=open(text_im,"r")
#opens the correct file

text=f.read()

text_out=input("Enter the output filename:\n")
g=open(text_out,"w")

#n_text=text.replace("\n\n","chr(1)")
n1_text=text.replace("\n"," ")
#n2_text=n1_text.replace("chr(1)","\n\n")

length_of_line=eval(input("Enter the line width:\n"))
#prints the length you want
words= n1_text.split(" ")

f.close()
lin_counter =1
# go through list of words and check if it should be on that line or not
for word in words :
    len_w=len(word)
    
    
    if (lin_counter+len_w) <=length_of_line :
        print(word,end=" ",file=g)
        lin_counter+=len_w +1
        
    else :
        print(file=g)
        print(word,sep="",end=" ",file=g)
        
        lin_counter=1 + len_w
    
    
g.close()