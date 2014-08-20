#Question 1
# Printing the entered string without duplicates
# By: Dean de Haast


def main():
    word =""
    print("Enter strings (end with DONE):")
    words=[]
    found =False
     
    
    # Creating the sentinel
    while word != "DONE":
              
        word =input()
        words.append(word)
    
    #Going through each position in the list
    print()
    print("Unique list:")
    for i in range(len(words)):
        # Checking if the word is entered somewhere else in the list.
        for x in range(i+1,len(words)):
            if words[i] == words[x]:
                words[x] = ""
                
        if words[i] != "" and words[i] != "DONE":
            print(words[i])
                
main()