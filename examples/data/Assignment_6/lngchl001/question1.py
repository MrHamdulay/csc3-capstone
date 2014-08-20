#function to print a list of strings, right alined
# by Chloe Longmore
# 22 April 2014


def string_list():
    print("Enter strings (end with DONE):")
    list_str=[]
    while True:
        list1=input("")
        if list1=='DONE':
            break        
        list_str.append(list1)
    #finding length of longest string in the list
    max_len=0
    for i in list_str:
        len_str=len(i)
        if len_str>=max_len:
            max_len=len_str


    #priting list right-aligned
    print()
    print("Right-aligned list:")
    for i in list_str:
        
        print('{0:>{1}}'.format(i,max_len))

string_list()