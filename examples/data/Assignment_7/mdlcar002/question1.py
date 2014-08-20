#Assignment 7 Question 1
#printing a list of strings in the same order without duplicates
#Carissa Moodley MDLCAR002

def main ():
    strings=[]#creating an empty list to store strings
    print("Enter strings (end with DONE):")#prompting the user to input strings
    
    string=input() #allows the user to enter a string
    
    while string!="DONE": #the user can keep entering strings until DONE is entered
        
        if (string not in strings): #checks if the string has been inputed before
            strings.append(string) #adds string to list of string
        string=input() #allows user to enter another string
        
    print("\nUnique list:")
    for i in strings:
        print(i)
        
main()