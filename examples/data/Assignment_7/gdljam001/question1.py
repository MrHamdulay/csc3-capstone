"""Enter strings delete duplicates print
James Godlonton
29 April 2014"""

def main():#Main function get input of strings and print unique ones
    print("Enter strings (end with DONE):\n")
    count=0
    words=[]#array is used to keep order
    newWord=input("")#get first string
    #append to array
  
    while(newWord!="DONE"):#while "DONE" sentinal not entered get new word
        
        if newWord not in words:#if new word not done and not already in the words array add it to array
          
            words.append(newWord)        
        newWord=input("")
        
  
    print("Unique list:")    
    for wrd in words:#Cycle through array printing words in correct order
        print(wrd)

if __name__=="__main__":#Running main
    main()