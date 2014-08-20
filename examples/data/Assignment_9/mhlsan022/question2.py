'''This program reformats a text file so that all lines are at most a given length
Sandile Mahlangu
13 May 2013'''
import textwrap
def print_file():
    '''This function accesses a text from a file and prints out a reformmatted text in an output file with given length'''
    input_file=input('Enter the input filename:\n') #The file which we get the text from
    filename=input('Enter the output filename:\n') #The file where we print out the formatted text
    length=eval(input('Enter the line width:\n'))  #The length which is needed
    
    #Open the file where the program will get the text
    file_text=open(input_file,'r')
    list_text= file_text.read()
    file_text.close()
    output= open(filename,'w')  #The file where everything will be printed in 
    paragraph_list= list_text.split('\n\n') #Splitting the file across paragraphs
    
    #Move through the paragraphs and reformat them and then print them into the output file
    for paragraph in paragraph_list:
        
        #Removing new line characters and replacing the with a space
        paragraph=paragraph.replace('\n',' ')
        #Reformating the paragraph
        paragraph=textwrap.wrap(paragraph,width=length)
        
        for printing in paragraph:
            #printing out each reformatted string
            print(printing, file=output)
        print(file=output)
    
    output.close()
if __name__=='__main__':
    print_file()