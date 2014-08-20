#Question 2
#Reformating a file to a given length
#By: Dean de Haast

#Opening the files
filename_in=input("Enter the marks filename:\n")
filename_out=input("Enter the output filename:\n")
f_in= open(filename_in, "r") 
f_out = open(filename_out, "w")
temp = ""

width =eval(input("Enter the line width:\n"))
words=[]
f =f_in.read()
f_in.close()
count =0

#Adding the words to a list
temp=f.replace("\n"," ")
words=temp.split(" ")


#Adding each newline to the file
while count < len(words):       #Going through all the words in the list
        newstring=""
        while len(newstring)+ len(words[count]) < width:        #Seeing if the new word can fit on the line
                newstring += words[count] + " "
                count+=1
                if count == len(words):
                        break   #Breaking out of the loop if all the words have been entered
        print(newstring,file=f_out)
        
f_out.close()