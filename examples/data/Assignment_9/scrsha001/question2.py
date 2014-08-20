#Shaaheen Sacoor SCRSHA001
#13 May 2014
#Program to format to text to a specific width

def main():
    inputf = input("Enter the input filename:\n")    # Get inputs
    input_new = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    f= open(inputf,"r")
    file_lines = f.readlines()
    for i in range(len(file_lines)):     #Since the split function will get rid of the "\n" for a new paragraph
        if file_lines[i] == '\n':        # I have temporarily changed the "\n" so as to know when theres a new paragraph
            file_lines[i] = "%"
            
    
    word_list = []
    for i in range(len(file_lines)):
        word_list += file_lines[i].split(" ")  #Add words to list, used .split(" ") so as to get the spaces
    for i in range(len(word_list)):     # As .split also gets rid of the spaces so to keep spaces 
        if word_list[i] == "":          # I have kept a temporary placeholder  
            word_list[i] = "@"     
            
    word_list = " ".join(word_list)         #Now join the list with the placeholders 
    word_list = word_list.split()           # And split it again but now i know where the double spaces and paragraphs are
    
    for i in range(len(word_list)):
        if word_list[i] == "@":         #Change placeholder back
            word_list[i] = ""
            

    counter = 0              # Counter keeps record of the length of words and spaces so as to know when to go to new line
    list_N = []
    for i in range(len(word_list)):            #Checks where sentence should end and start on a new line
        if word_list[i] == "%":                # Starts counter to zero as "%" means the end of a paragraph and a new line
            counter = 0 
        elif (counter + len(word_list[i]) ) > width:  #If the addition of the length of a word is greater than the width 
            list_N.append(i)                          # Append the position to a list and reset counter
            counter = 0
            counter = counter + len(word_list[i]) + 1
          
        else:
            counter = counter + len(word_list[i]) + 1

     
    new_file = open(input_new,"w")
    list_N.insert(0,0)       
    changer = True
    for i in range(len(list_N)):                   #Prints to new document, Starts on new line on the positions
        if i == (len(list_N)-1):                   #Previously recorded
            for f in range(list_N[-1],len(word_list)):
                    print(word_list[f],end=" ",file = new_file)          
                
        else:
            for j in range(list_N[i],list_N[i+1]):
                if word_list[j] == "%":        #"%" indicates paragraph
                    print(file=new_file)
                    print(file =new_file)
                    changer = False
                else:
                    print(word_list[j],end=" ",file = new_file)
                    changer = True
                    
        if changer is True:
            print(file = new_file)

main()