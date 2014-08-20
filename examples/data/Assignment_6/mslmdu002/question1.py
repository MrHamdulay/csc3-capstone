"""This programs takes a list of strings and then print out the strings right aligned with the longest
Masilela Mduduzi
22 April 2014"""
string_list = [ ]
def main():
    string=input("Enter strings (end with DONE):\n\n")

    string_list = [ ] #an empty list
    
    string_list.append(string)  #adding users input to the string    
    
    while "DONE" not in string_list:

        string=input("") #if input !=DONE invoke the user again
        string_list.append(string)#store the new input into string_list 

    string_list.remove("DONE") #if done found ,remove DONE in the list

    max=0 #initialise  maximum lenght
    for i in string_list:

        if len(i)>max:#check if the lenght of the word is higher than the previous 1
            max=len(i)
    
    print("Right-aligned list:")

    for i in range(len(string_list)):

        Right_aligned= string_list[i].rjust(max)#align the strings in the right
        print(Right_aligned)

if __name__ == "__main__":
    main()
