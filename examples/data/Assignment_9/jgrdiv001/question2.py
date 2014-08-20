"""program to reformat a text file to set width lines
author: Divan Jagers
Date: 12 May 2014"""
def Reformat():
    F_input=input("Enter the input filename:\n")     #prompts the user for inputs, outputs and width parameters
    F_output=input("Enter the output filename:\n")    
    width=eval(input("Enter the line width:\n"))
    f=open(F_input,"r")     #opens the file and reads
    data=f.read()    #list is created with the input content
    f.close()         #file is closed
    list1=data.split(" ")    #it then creates a list1 with each individual word in the content of the file
    length= 0    #a length counter of the sentence line length
    list2=[]
    n_list=[]      # list with all "\n" characters removed and only "\n\n" characters retained for ease when working with paragraphs and therefore this list is a linear representation of the words in the file that was read
    for k in list1:   #an iteration that adds items to n_list
        if k.count("\n\n")==1:
            n_list.append(k+" ")
            continue
        else:
            for j in k.split("\n"):
                n_list.append(j+" ")
    for j in range(len(n_list)):    #iteration that loops through n_list and creates a new list2 that will basically now split the content into the desired format
        if n_list[j]=="\n\n":
            length=0
        elif length + len(n_list[j])<=width :
            length+=len(n_list[j])
            list2.append(n_list[j])
        else:
            length=len(n_list[j])
            list2.append("\n")
            list2.append(n_list[j])
    f=open(F_output,"w")
    for item in list2:
        print(item,end="",file=f)   #prints list2 into the output file
    f.close()
if __name__=="__main__":
    Reformat()