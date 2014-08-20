'''program to allow user to enter a list of items and then print out the list without all the duplicates
Wandile Khowa
01-05-2014
'''
def list_entry():
    final_list = [] #creates an empty list to store non-duplicates
    ques = input("Enter strings (end with DONE): \n")
    while ques != "DONE":   #creates a sentinel
        if ques not in final_list:  #checks to see if word is not in the created list
            final_list.append(ques) #adds unique word into list
            ques = input("")
        else:
            ques = input("")

    print("\nUnique list:")
    for i in final_list:
        print(i)
    
if __name__=="__main__":
    list_entry()
        