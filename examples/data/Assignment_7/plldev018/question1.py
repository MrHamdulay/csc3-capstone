# Print strings without duplicates
# Devaksha Pillay
# 27 April 2014

words = input("Enter strings (end with DONE):\n")

#create an empty string
words_list = []

#enter multiple inputs and store them in a list
while words != "DONE":
    words_list.append(words)
    words = input ()

#list with no repeats
no_repeats = []

for item in words_list:
    if not item in no_repeats:
        no_repeats.append(item)

#print the unique list
print()
print("Unique list:")

for item in no_repeats:
    print(item)