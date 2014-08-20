#Question 1
#Entering a list of strings, right allignment
#By: Dean de Haast

def main():
   
    longest=0
    current_word =""
    words=[]
    print("Enter strings (end with DONE):")
    
    #Adding words to the list
    while current_word != "DONE":
        words.append(current_word)
        current_word=input()             
    #Finding the longest word    
        if len(current_word)> longest:
                longest =len(current_word)
    #Printing the output layouot
    print()           
    print("Right-aligned list:", end="")
    #calculating the spaces for each item in the list
    for i in range (len(words)):
        spaces=longest-len(words[i])     
        print(" "*spaces + words[i])
main()