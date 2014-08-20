# 22 April 2014
# Tayla Radmore
# Formatted columb


#intial word
list_of_words=[]
word=input("Enter strings (end with DONE): \n")
if word=="DONE":
    print()
    print("Right-aligned list:")    

else:
    
    list_of_words.append(word)
    next_word=""

    #adding more words
    while next_word != "DONE":
        next_word=input()
        list_of_words.append(next_word)
    
        #removing DONE
    index_to_remove=len(list_of_words)-1
    del list_of_words[index_to_remove]
    #making spacing
    max=0
        
    for i in list_of_words:
        length=len(i)
        if length>max:
            max=length

    print()
    print("Right-aligned list:")


    #printing the words

    for i in list_of_words:
        spacing=max - len(i)
        print(" "*spacing,i,sep="")
    
    
