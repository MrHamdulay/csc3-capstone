""" Bella gorham
right align strings
20/04/2014"""


# make empty list
words = []
# make empty string
string = ""
maxlength = 0
# make ask fpr new string until DONE
print("Enter strings (end with DONE):")
while string != "DONE":
    
    string = input()
    if string == "DONE":
            break    
    words.append(string)
    
    # find max length
    length = len(string)
    
    if maxlength < length:
        maxlength = length

        



print()
print("Right-aligned list:")
# print all strings right
for i in words:
    
    length = len(i)
    spaces = maxlength - length
    print(" "*spaces + i )
    
    
        
            

    
