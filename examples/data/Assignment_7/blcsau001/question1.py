#Code to print out string without duplicates
#Saul Bloch
#27 April 2014

words = input("Enter strings (end with DONE):\n")
#creating word array
word_Array=[]

#Adding unique words to array
while words != "DONE":
    if words not in word_Array:
        word_Array.append(words)
    words=input("")

#printing unique list
print()
print("Unique list:")
for i in range (len(word_Array)):
    print(word_Array[i])
