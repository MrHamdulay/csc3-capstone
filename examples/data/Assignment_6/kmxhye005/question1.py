# Program to print out right-aligned list of strings with the longest string when a list of strings are entered followed by "DONE"


def Name_list():    #Getting the name lists
    name_lists = []
    in_put = input("Enter strings (end with DONE): \n")
    while in_put != "DONE":
        name_lists.append(in_put)
        in_put = input("")
    return name_lists


def Finder(name_lists):   # Aligning to the right
    newnamelist = []
    indices = 0
    for i in name_lists:
        in_put = len(name_lists[indices])
        newnamelist.append(in_put)
        indices += 1
    newnamelist.sort()
    newnamelist.reverse()
    return newnamelist[0]



a = Name_list()
b = Finder(a)
print()


def Right_aligner(name_lists, maximum):   # Making space/print, using max number
    print("Right-aligned list: ")
    for i in name_lists:
        gap = maximum - len(i)
        print((" "*gap)+i)

        

Right_aligner(a,b)