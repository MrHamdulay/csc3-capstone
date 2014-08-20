"""Files: reformat a given text file according to given length
danica van der zandt
11 may 2014"""

#print the given input text into one line

##how am i supposed to take a paragraph and see it as an input?

text=input()
given_text=[]
while text:
    given_text.append(text)
    
    text=input()
given_text=" \n ".join(given_text)

#print the long string input to the file
f=open("input.txt","w")
print(given_text,file=f)
f.close()


#get input filename and retrieve the lines within
input_text=input("Enter the input filename:\n")
f=open(input_text,"r")
text=f.readline()
f.close()

#get the filename for output 
output_text=input("Enter the output filename:\n")
f=open(output_text,"w")
print("",end="",file=f)
f.close()

#reformatting the file
def formatted_text(text):
    temp_text=text.split(" ")
    
    length_text=len(text)
    if len(text)<=width:
        f=open(output_text,"a")
        for line in temp_text:
            print(line+" ",end="",file=f)
        f.close()         
        
    
    else:
        lines=[]
        temp_list=[]
        temp_length=0
        for word_length in temp_text:
            length=len(word_length) + 1
            if temp_length + length <= width:
                temp_length+=length
                temp_list.append(word_length)
                              
            
            else:
                lines=temp_list
                f=open(output_text,"a")
                for line in lines:
                    print(line+" ",end="",file=f)
                print("\n",end="", file=f)
                f.close()                 
                text=text[temp_length:]
                return formatted_text(text)
       
        
width=int(input("Enter the line width:\n"))
formatted_text(text)


##do i need to print the output file to the screen?
#f=open(output_text,"r")
#print(f.readlines())
#f.close()
