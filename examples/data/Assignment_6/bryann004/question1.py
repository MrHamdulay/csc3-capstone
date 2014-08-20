# Anna Borysova
# Assignment 6, Question 1
# 2014-04-22

# initialise variables
strings = []
input_string = ""
max_length = 0
#get strings, find max length
print("Enter strings (end with DONE):")
while True:
    input_string = input("")
    if input_string == "DONE":
        break
    strings.append(input_string)
    if len(input_string) > max_length:
        max_length = len(input_string)
        
# align and print
print("\nRight-aligned list:")
for string in strings:
    print(("{:>" + str(max_length) + "}").format(string))
