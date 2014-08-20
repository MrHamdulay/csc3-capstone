# program to simulate a BBS 
# hendrik Joosten
# 17 april 2014

#initially define variable and error messages
user_msg = "no message yet"
user_input = "a"
file_not_found_err = "File not found"

# while loop to repeat the program until the user chooses to exit
while user_input != "x" and user_input != "X":
      
      # printing the menu
      print("Welcome to UCT BBS")      
      print("MENU")
      print("(E)nter a message")
      print("(V)iew message")
      print("(L)ist files")
      print("(D)isplay file")
      print("e(X)it") 
      
      # geting the users input
      user_input = input("Enter your selection:\n")
      
      # if the user wants to enter a message
      if user_input == "E" or user_input == "e":
            user_msg = input("Enter the message:\n")
      
      # if the user wants to view he entered message      
      elif user_input == "V" or user_input == "v":
            print("The message is: "+user_msg)
            
      # list the files in a directory (due to my limited knowledge of files in 
      # python i just simulated this output with a print function)
      elif user_input == "L" or user_input == "l":
            print("List of files: 42.txt, 1015.txt")
            
      # if the user wants to display a file                                 
      elif user_input == "D" or user_input == "d":
            filename = input("Enter the filename:\n")            
            if filename == "42.txt":
                  print("The meaning of life is blah blah blah ...")
            elif filename == "1015.txt":
                  print("Computer Science class notes ... simplified")
                  print("Do all work")
                  print("Pass course")
                  print("Be happy")
      # failsafe if the user selects a file that does not exsist
            else:
                  print(file_not_found_err)
                  
      # due to my limited knowledge of files in python i 
      # just simulated these outputs with a print functions 
      
      # if the user chose to exit the program
      elif user_input == "X" or user_input == "x":
            print("Goodbye!")
