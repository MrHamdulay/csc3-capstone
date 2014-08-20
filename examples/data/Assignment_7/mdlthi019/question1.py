"""Program to remove repetitions in a list
Thiloshni Moodley
30 April 2014"""

string=[]
word=input("Enter strings (end with DONE):\n")
while word != "DONE": #proceeds if not done
    string.append(word) #adds the input to the list
    word=input("")
print("\nUnique list:")
    
string_2 = []    #create new empty list 
for word_2 in string:
    while word_2 not in string_2:
        string_2.append(word_2) #new list without the repetition of words
for j in string_2:
    print(j)
