sentence = ""
print ("Enter strings (end with DONE):")
print ()
string = ""
string_length = 0
max_str_len = string_length
#Input list of strings with their respective lengths in strings dictionary
while string != "DONE":
    string = input()
    if string == "DONE": break
    string_length = len(string)
    sentence += "\n" + string
    if string_length > max_str_len: max_str_len = string_length
    
strings = sentence[1::].split("\n")
#Output right-aligned list of strings
print("Right-aligned list:")
template = "{0:>" + str(max_str_len) + "}"
for String in strings:
    print(template.format(String))