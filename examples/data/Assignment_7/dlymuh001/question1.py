print ("Enter strings (end with DONE):")
string_set = [] #Stores all strings that are input by user but without duplicates until DONE is entered
string = ""

while string != "DONE":
    string = input()
    if not (string in string_set) and string != "DONE":
        string_set.append(string)
print()
print("Unique list:")
for i in string_set:
    print(i)