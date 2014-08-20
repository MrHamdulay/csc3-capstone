# printing a list with no repeats
# Tayla Radmore
# 30 April 2014

#getting inputs
list_of_words=[]
word=input("Enter strings (end with DONE): \n")
list_of_words.append(word)
while word!="DONE":
    word=input()
    list_of_words.append(word)
#removing done
index_to_remove=len(list_of_words)-1
del list_of_words[index_to_remove]
           
#counting the votes
final_words=[]
for i in list_of_words:
    if i not in final_words:
        final_words.append(i)

# printing the list
print()
print("Unique list:")        
for i in final_words:
    print(i)
    





