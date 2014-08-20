# question1.py
# a program where the user can entera list of strings followed
# by a sentinel "DONE" and the list of strings is then printed
# out right-aligned witht the longest string.
# Thomas Konigkramer
# 20 April 2014

def right():
    # asking for input
    list_of_strings = input("Enter strings (end with DONE):\n")
    
    # creating list with first input as content 
    array = [list_of_strings]

    # asking for input and adding to list until DONE entered
    while list_of_strings != "DONE":
        list_of_strings = input()
        array.append(list_of_strings)
    
    array.remove("DONE")
    string_max = 0 # to record length of longest string in array
    for i in range(len(array)):
        if len(array[i]) > string_max:
            string_max = len(array[i])
        
    print()
    print("Right-aligned list:")
        
        # number of letters/digits in the largest   no. in array
    for j in range(len(array)):
        print(array[j].rjust(string_max))
         
if __name__ == "__main__":
    right()
    
  