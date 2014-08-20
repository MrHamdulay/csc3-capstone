#kereshnee pillay
# 22pril 2014
#strinf=gs and lists


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