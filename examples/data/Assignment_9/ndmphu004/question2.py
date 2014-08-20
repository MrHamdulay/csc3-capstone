#Phumelele Ndimande
#Assignment 9


#Variables and input
inputname = input("Enter the input filename:\n")
outputname = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))


def reformat(inputname, width, outputname):
    #variables within function
    para = ""
    counter = 0
    para_formatted = ""
    count = 0
    
    
    #input file reading of it
    f = open(inputname, "r")
    lines = f.readlines()
    f.close()
    #working with the lines
    #getting all of them into a list
    for i in lines:
        count = 0
        for word in i:
            #if word given is a space then it should remain there
            if word == " ":
                para = para + word
            #if it is the last word in the word i line
            elif (word == "\n") and (word == i[-1]):
                para = para + " +++ "
            #if it isn't the last thing, it makes it complex because it could be another space/enter
            elif word == "\n":
                #this is for when there is an enter again
                if count + 1 <= 2:
                    para = para + " "
                    count = count + 1
                else: 
                    para = para + " +++ "
                    count = 0   
            elif ("\n" not in word):
                para = para + word   
    #Just to check that there are no funny stuff being supplied to textfile
            else:
                para = para + word + "!"   
   #clearing new file
    f = open(outputname, "w")
    f.close()
    
    #working with new file
    f = open(filename_out, "a")
    
    #creating an array of the list so as to print into new file
    para_list = para.split(" ")
    word = ""
    for i in (para_list):
        #just a word, not next line
        if (i == '') and (word == "+++") : 
            para_formatted = para_formatted + "\n\n"
            count= 0
            counter = 0
            word = i
        elif (len(i)+ counter <= width) and (i != "+++"):
            para_formatted = para_formatted + i + " "
            counter = counter + len(i) + 1
            count = 0
            word = i
        #next line      
        elif (i == "+++"):  
            if count >=2:
                para_formatted = para_formatted + "\n"
                counter = 0
                count =0
                word = i
            else:
                para_formatted = para_formatted
                count = count + 1
                word = i
        #word adding will be too great
        elif (len(i) + counter > width) and (i != "++" ):
            para_formatted = para_formatted + "\n" + i + " "
            counter = len(i) + 1   
            count = 0
            word = i
               
    print(para_formatted, file = f)
    f.close()
 
#running the program         
reformat(inputname, width, outputname)
