""" Program to reformat a text file to a given length
Khanyisile Morudu
15 May 2014""" 


#Variables and input
filename_in = input("Enter the input filename:\n")
filename_out = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))


def reformat(filename_in, width, filename_out):
    #variables within function
    para = ""
    counter = 0
    para_formatted = ""
    count_space = 0
    
    
    #input file reading of it
    f = open(filename_in, "r")
    lines = f.readlines()
    f.close()
    #working with the lines
    #getting all of them into a list
    for i in lines:
        count_space = 0
        for word in i:
            #if word given is a space then it should remain there
            if word == " ":
                para = para + word
            #if it is the last word in the word i line
            elif (word == "\n") and (word == i[-1]):
                para = para + " ^^^ "
            #if it isn't the last thing, it makes it complex because it could be another space/enter
            elif word == "\n":
                #this is for when there is an enter again
                if count_space + 1 <= 2:
                    para = para + " "
                    count_space = count_space + 1
                else: 
                    para = para + " ^^^ "
                    count_space = 0   
            elif ("\n" not in word):
                para = para + word   
    #Just to check that there are no funny stuff being supplied to textfile
            else:
                para = para + word + "!"   
   #clearing new file
    f = open(filename_out, "w")
    f.close()
    
    #working with new file
    f = open(filename_out, "a")
    
    #creating an array of the list so as to print into new file
    para_list = para.split(" ")
    word = ""
    for i in (para_list):
        #just a word, not next line
        if (i == '') and (word == "^^^") : 
            para_formatted = para_formatted + "\n\n"
            count_space = 0
            counter = 0
            word = i
        elif (len(i)+ counter <= width) and (i != "^^^"):
            para_formatted = para_formatted + i + " "
            counter = counter + len(i) + 1
            count_space = 0
            word = i
        #next line      
        elif (i == "^^^"):  
            if count_space >=2:
                para_formatted = para_formatted + "\n"
                counter = 0
                count_space =0
                word = i
            else:
                para_formatted = para_formatted
                count_space = count_space + 1
                word = i
        #word adding will be too great
        elif (len(i) + counter > width) and (i != "^^" ):
            para_formatted = para_formatted + "\n" + i + " "
            counter = len(i) + 1   
            count_space = 0
            word = i
               
    print(para_formatted, file = f)
    f.close()
 
#running the program         
reformat(filename_in, width, filename_out)
