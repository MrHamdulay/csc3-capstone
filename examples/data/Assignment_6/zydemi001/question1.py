#A program where the user can enter a list of strings and then print the list out, right-aligned with the longest string
#Author: Emiel Zyde
#Date: 20 April 2014

string1 = input("Enter strings (end with DONE):\n")
list_strings = []  #intializing accumulator variable

while string1 != "DONE":  #continue to get input until user enters DONE
    list_strings.append(string1) #build up the string
    string1 = input("")



max_length = 0  #setting the length of the longest string equal to 0

for i in list_strings:   #find the maximum length of a string given
    if len(i) > max_length:
        max_length = len(i)

print("\nRight-aligned list:")
for i in list_strings:  #printing each input right-justified in a column width equal to the length of the longest string
    print(i.rjust(max_length))
    