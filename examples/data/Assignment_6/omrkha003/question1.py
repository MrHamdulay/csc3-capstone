# program to right-align a list of strings with the longest string
# khadeejah omar
# 20 april 2014

string_list = []
string = input("Enter strings (end with DONE): \n") # prompts user to enter the first name

if string != "DONE" :
        string_list.append(string) 
        max_length = len(string) # sets length of first name to be the maximum

        while string != "DONE" :
                string = input("") # prompts user to enter another name
                if string != "DONE" :
                        string_list.append(string)
                length = len(string)
                if length > max_length : # if the name is longer than the previously entered name, set its length to be the maximum
                        max_length = length
        
        alligned_list = []
        # right-alligns each name according to the longest name
        for name in string_list :
                name = (" " * (max_length - len(name))) + name  # adds space needed to for the name be right-aligned
                alligned_list.append(name)

        s = "\n".join(alligned_list)

        print()
        print("Right-aligned list: \n" + s) # prints right-aligned names
else : # if no names were entered
        print()
        print("Right-aligned list: ")