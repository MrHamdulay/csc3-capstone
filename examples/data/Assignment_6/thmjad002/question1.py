"""Assignment 6 Question 1
JT
22-04-2014"""


def get_list():
    string = input("Enter strings (end with DONE):\n")
    global maxlen
    maxlen = len(string)
    list1 = []
    while string != "DONE":
        list1.append(string)
        string = input()
        if len(string) > maxlen:
            maxlen = len(string)
    return list1

def right_align():
    global maxlen
    #right_aligned_string = ''
    a = get_list()
    print("\nRight-aligned list:")
    for name in a:
        #print("{0:>a}".format(name))
        width = maxlen
        #print(width)
        name = str(name)
        print(name.rjust(width))
        #right_aligned_string += " "*(maxlen - len(name)) + name + chr(13)
    #print("\nRight-aligned list:",right_aligned_string,sep="\n")   

right_align()