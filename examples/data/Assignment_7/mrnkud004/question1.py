"""Enter strings delete duplicates print
Kennedy muranda
2 May 2014"""

#Main function get input of strings and print unique ones
def main():
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

#Running main
if __name__=="__main__":
    main()