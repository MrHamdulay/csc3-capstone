""" unique list
alexander Whiting
30 april 2014"""

words = []

print("Enter strings (end with DONE):\n")
word = input("")

while word != "DONE":
    if word not in words:
        words.append(word)
    word = input("")

print("Unique list:")

for i in words:
    print(i)
