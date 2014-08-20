"""Ailsa Mackay MCKAIL001
Assignment 7 Question 1
2014-04-29"""

def no_duplicates():
    word_list=[]
    item = input("Enter strings (end with DONE):\n")
    while item != "DONE": 
        if item in word_list: #check to see whether the item has already been added to the list
            item=input("")
        else: 
            word_list.append(item)
            item=input("")
    print("")
    print("Unique list:")
    for i in word_list:
        print(i)

no_duplicates()

            