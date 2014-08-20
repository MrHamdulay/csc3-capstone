import os
import sys


def displayMenu ():
	print ("Welcome to UCT BBS")
	print ("MENU")
	print ("(E)nter a message")
	print ("(V)iew message")
	print ("(L)ist files")
	print ("(D)isplay file")
	print ("e(X)it")
	print ("Enter your selection:")
	value=input("")
	
	return value;

def main ():
	
	#clear the screen before starting
  #os.system('cls' if os.name == 'nt' else 'clear')

  #Exit condition for while loop
  stop = 1
  
  #value to be displayed for List Files
  fileNames = "List of files: "
  
  #delimiter for List Files
  comma = ""
  
  msg="no message yet"
  
  #Retrieve the files names ending in txt from the current folder where the program is running
  files = [f for f in os.listdir('.') if f.endswith('.txt')]
  
  #order the files to get 42.txt before 1015.txt and join it to the variable fileNames
  for f in sorted(files, reverse=True):
    fileNames = fileNames + comma + f
    comma = ", "
      
  while stop == 1:
    
    val=displayMenu ()

    #Exit if x or X is inputed    
    if val.lower() == 'x':
      stop = 0
    elif val.lower() == 'e':
      print ("Enter the message: ")
      msg=input("")
    elif val.lower() == 'v':
      print ("The message is:",msg)
    elif val.lower() == 'l':
      print (fileNames)
    elif val.lower() == 'd':  
      print ("Enter the filename:")    
      filename=input("")
      try:
        f = open(filename, 'r')
        print (f.read())
        f.close()
      except IOError:
        print ("File not found")
      
  else:
    print ("Goodbye!")
    


if __name__ == "__main__":
   main()
