""" Program to format file to given width
Onalerona Mosimege
13 May 2014""" 



#Entries by user
filename_in = input("Enter the input filename:\n")
filename_out =input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

def format(filename_in, width, filename_out):
#initialize  variables dor the total character length of string, for the string that will be split into an array and for the output paragraph  
    para = ""
    counter = 0
    para_formatted = ""
    count_space = 0
    
    
    #read file
    f = open(filename_in, "r")
    lines = f.readlines()
    f.close()
   #check for \n
    for i in lines:
        count_space = 0
        for word in i:
            if word == " ":
                para = para + word
            elif (word == "\n") and (word == i[-1]):
                para = para + " ^^^ "
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
            else:
                para = para + word + "!"
   
    f = open(filename_out, "w")
    f.close()
    
    #working with new file
    f = open(filename_out, "a")
    
    #creating an array of the list so as to print into new file
    para_list = para.split(" ")
    print(para_list)
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
        elif (len(i) + counter > width) and (i != "^^^" ):
            para_formatted = para_formatted + "\n" + i + " "
            counter = len(i) + 1   
            count_space = 0
            word = i
            
    print(para_formatted, file = f)
    f.close()
         
format(filename_in, width, filename_out)
