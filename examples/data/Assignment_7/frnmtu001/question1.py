"""This program takes in a list of strings and then prints them out without duplicating any
Mtunzi France
28 April 2014"""

def words():
    """Create two lists to add the words to"""
    words = []
    words_to_print = []
    strings = input("Enter strings (end with DONE):\n")
    print("")
    words.append(strings)
    #if the user types in DONE from the very beginning
    if words[0] == "DONE":
        print("Unique list:")
        print("")
        """Continues to ask for input until the word DONE is entered"""
    else:
        while "DONE" not in words:
            more_strings = input()
            words.append(more_strings)
        words.remove("DONE") #removes DONE from the list
        for i in words:
            """Adds the words in the first list to the second list,and does not duplicate any words"""
            if i not in words_to_print: 
                words_to_print.append(i)
            """Prints the words in the second list"""
        print("Unique list:")
        for i in words_to_print:
            print(i)
words()