"""User enters a list of strings followed by a sentinal
Chris Bolton """

print ("Enter strings (end with DONE):")
user_input = ""
list_words = []
sentinel = "DONE"
while user_input != sentinel: #user can input names untill they enter "DONE"
    user_input = input()
    list_words.append(user_input)

max_letter = 0

for i in range (len(list_words)-1): #loop through to detirmine string with greatest amount of letters
    if len(list_words[i])>max_letter:
        max_letter = len(list_words[i])

print ("\nRight-aligned list:")

for j in range (len(list_words)-1):
    print (" "*(max_letter-len(list_words[j]))+list_words[j])