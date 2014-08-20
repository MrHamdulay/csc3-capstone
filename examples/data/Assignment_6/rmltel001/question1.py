"""Program where the user can enter a list of strings followed by the sentinel
"DONE" and the list of strings is then printed out right-aligned with the
longest string.
Telisha Ramlall
20 April 2014"""

#Declare list
words = []

#Get strings
word = input("Enter strings (end with DONE):\n")
while word.lower() != "done":
    words.append(word)
    word = input()

#Find longest word
longest = 0
for word in words:
    if len(word) > longest:
        longest = len(word)

#Insert spaces in front of each word in array until length equals the longest word
print("\nRight-aligned list:")
for word in words:
    while len(word) < longest:
        word = " " + word
    print(word)