#Enter strings delete duplicates print
#Anthony Jacob
#02 May 2014

def main():#Main function to get input of strings and print unique ones
    print("Enter strings (end with DONE):\n")
    count=0
    words=[]#array is used to keep order
    new_word=input("")# to get the first string
    #append to array
  
    while(new_word!="DONE"):#while sentinal "DONE" not entered get new word
        if new_word not in words:
            words.append(new_word)        
        new_word=input("")
  
    print("Unique list:")    
    for wrd in words:#Cycle through array printing words in correct order
        print(wrd)

if __name__=="__main__":#Running main
    main()