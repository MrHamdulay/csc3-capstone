""" a program that takes in words and prints them all except those wit duplicates
nelisile mkhwebane
30/04/2014 """

""" create an empty list """
list_words = []

""" get the string of words from the user """

string_words = input ("Enter strings (end with DONE):\n")

""" while the input is not "DONE", must continoue entering"""
while string_words != "DONE":
    list_words.append(string_words)
    string_words = input()

""" to get the unique words """
count = []
for word in list_words:
    if word not in count:
        count.append(word)
    else:
        continue
#counts= {}
#for w in list_words:
    #counts[w] = counts.get(w,0)+1
#unique_list = list(counts.keys())

""" printing out the output """
print("")
print("Unique list:")

for w in count:
    print(w)
