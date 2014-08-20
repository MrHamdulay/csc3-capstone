"""this program to stimulate simple Bulletin Board Systems with one stored message and two fixed files
20/04/20
Tsitsi Karimkawenda"""


message="no message yet"
file1="42.txt"
file2="1015.txt"
selection=""
while True:
    print("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")
    selection = input("Enter your selection: \n") 
    #this while loop is used to type all that is written above to re-iterate after user has inputted respective message
    
   
    
    if selection == "E" or selection == "e": #this condition needs to execute if the user has chosen e/E, enabled by the or statement user prints in message and thus the default message will be updated
        message = input("Enter the message: \n")
         
    elif selection == "V" or selection == "v":#this condition will enable user to veiw the massage
       
        print("The message is:",message )        #the message updated or not will be on display
     
    elif selection == "L" or selection == "l": #if user selects l/L, enabled by or staement the files will be listed
        print("List of files: ",file1,", ",file2,sep="")
                       
    elif selection == "D" or selection == "d": #when this portion is chosen the user has an option to open either file 1 or file 2 hence the nested loop
        file_info = input("Enter the filename: \n")
        if file_info == file1:
            print("The meaning of life is blah blah blah ...") #when file 1 is chossen this is made to display
        elif file_info == file2:
            print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")#if file2 is chosen this iformation will be put in display 
            
        else:
            print("File not found") #if non of the above conditions are met this is put on display
  
    elif  selection == "X" or selection == "x":
        print("Goodbye!")
        break #used to break out of the loop if this X condition is met(printed in by the user 
           
           
           
           
    
#def main(): #at bottom
#how is the iteration of the loop done wen i want all the welcome to uct etc to be done again?
#how is the default message done?