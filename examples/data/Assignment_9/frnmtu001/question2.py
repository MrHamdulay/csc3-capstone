"""This program formats a text-file to a given length
Mtunzi France
17 May 2014"""
def mtunzi():
    """Get filename from user and copy it's content to a list"""
    
    in_file_name = input("Enter the input filename:\n")
    File = open(in_file_name, "r") 
    list1 = []
    for i in File: #iterate trhough each line in the readed file
        list1.append(i)
    File.close()
    
    """Get name of output file from user and also the width"""
    OutFile = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    for i in range(len(list1)):
        if list1[i] == "\n":
            pass
        elif list1[i][-1:] == "\n":  #Removes the newline character
            list1[i] = list1[i][:-1]
            
    list2 = []
    for sentence in range(len(list1)):  #Iterate through the list with the words
        list1[sentence] = list1[sentence].split(" ")
        for word in range(len(list1[sentence])): #Iterate over each single word in the list
            list2.append(list1[sentence][word])  #add each word to the new list
            
    output_file=open(OutFile, "w") #create the output file
    empty = ""
    while True:
        try:  
            if list2[0] == "\n": #checks whether the line is empty
                empty = empty + list2[0]
                print(empty, file=output_file) # prints the original file if it's an empty string
                list2.remove(list2[0])
                empty =""
            elif empty =="":
                empty = list2[0] #add words to the line
                list2.remove(list2[0])
            elif len(empty+" "+list2[0]) <= width:
                empty = empty+" "+list2[0]
                list2.remove(list2[0])
            else:
                print(empty,file=output_file)                
                empty=""
        except:
            print(empty,file=output_file) 
            output_file.close()#close file
            break #stop the indefinite loop
        
mtunzi()