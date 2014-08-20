"""A program to right-align an inputted list
by Jeremy Smith
21 April 2014"""

#receive an input list of strings
name_list = []
string = input("Enter strings (end with DONE):\n")
name_list.append(string)
while string != "DONE":
    string = input("")
    name_list.append(string)
del name_list[-1]

#determine the length of the longest string
if name_list == []:
    print("\nRight-aligned list:")
else:
    max_namelength = len(name_list[0])
    for name in name_list:
        x=len(name)
        if x > max_namelength:
            max_namelength = x
#stipulate the format based on the longest string and print the list
    align="{0:>"+str(max_namelength)+"}"
    print("\nRight-aligned list:")
    for string in name_list:
        print(align.format(string))    