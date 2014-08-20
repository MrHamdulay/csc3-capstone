# Author : Rayaan Fakier FKRRAY001
# Date : 28 - 04 - 2014
# question1.py

def listing():
    '''Program which returns a list with each different entry returned once'''
    ori_list = []
    final_list = []
    entry = ""
    
    print("Enter strings (end with DONE):")
    # Takes string inputs -> appends to a list
    while entry != "DONE":
        entry = input()
        ori_list.append(entry) 
        
    ori_list.remove("DONE") # Removes str 'DONE'
    
    # Adds var entry only once to a list
    for entries in ori_list:
        if not entries in final_list:
            final_list.append(entries)
    
    # Prints each individual str
    print() 
    print("Unique list:")       
    for strings in final_list:
        print(strings)
    
listing()