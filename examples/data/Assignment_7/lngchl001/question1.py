#function that stores input words in a list, removes duplicates, and then prints them in the same order
#By Chloe Longmore
#1 April 2014

def words():
    print("Enter strings (end with DONE):")
    #create list for storing words
    words=[]
    while True:
        word= input("")
        #check for duplicated words
        if word in words:
            continue
        #check if the user wants to end input
        elif word=="DONE":
            break
        #add words to list
        else:
            words.append(word)
    #print out list of stored words 
    print()
    print("Unique list:")
    for i in words:
        print(i)
words()