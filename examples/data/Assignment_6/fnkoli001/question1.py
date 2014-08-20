strings = []

#Get input
input_string = input("Enter strings (end with DONE):\n")
strings.append(input_string)

while input_string != "DONE":
    input_string = input("")
    strings.append(input_string)
strings = strings[:-1]

#get biggest string len
max_len = 0
for string in strings:
    if len(string) > max_len:
        max_len = len(string)

right_alligned_strings = []

#Right alline the strigns
for string in strings:
    right_alligned_strings.append(" " * (max_len - len(string)) + string)

print()
print("Right-aligned list:")
print("\n".join(right_alligned_strings))