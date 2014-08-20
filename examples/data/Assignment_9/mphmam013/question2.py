"""Mphuthi Mamorena 
question2
assignment 9"""

filename=input("Enter the input filename:\n")
outfilename=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

def linesprint(filename, width, outfilename):
    v = ""
    u = 0
    v_formatted = ""
    spaces = 0
    

    f = open(filename, "r")
    lines = f.readlines()# reding lines as array
    f.close()
    for line in lines:
        spaces = 0
        for word in line:
            if word == " ": # empty spaces
                v = v + word
            elif (word == "\n") and (word == line[-1]): #checking for the last word in the line
                v = v + " ^^^ " # adding this to the end of each line
            elif word == "\n":
                if spaces + 1 <= 2:
                    v = v + " "
                    spaces = spaces + 1 
                else: 
                    v = v + " ^^^ "
                    spaces = 0   
            elif ("\n" not in word):
                v = v + word   
            else:
                v = v + word + "!"
                
                
                
    outfile=open(outfilename,"w")
    outfile.close()

    f = open(outfilename, "a")
    v_list = v.split(" ")

    word = ""
    for i in (v_list):
        
        if (i == '') and (word == "^^^") : 
            v_formatted = v_formatted + "\n\n"
            spaces = 0
            u = 0
            word = i
        elif (len(i)+ u <= width) and (i != "^^^"):
            v_formatted = v_formatted + i + " "
            u = u + len(i) + 1
            spaces = 0
            word = i
           
        elif (i == "^^^"):  
            if spaces >=2:
                v_formatted = v_formatted + "\n"
                u = 0
                spaces =0
                word = i
            else:
                v_formatted = v_formatted
                spaces = spaces + 1
                word = i
        elif (len(i) + u > width) and (i != "^^^" ):
            v_formatted = v_formatted + "\n" + i + " "
            u = len(i) + 1   
            spaces = 0
            word = i
            
    print(v_formatted, file = f)
    f.close()
         
linesprint(filename, width, outfilename)





