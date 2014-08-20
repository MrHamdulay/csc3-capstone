word=""
lists_words=[]
words=input("Enter strings (end with DONE): \n")
lists_words.append(words)
while words !="DONE":
    words = input()
    lists_words.append(words)
def uniqlist(unsorted):
    unique_words = []
    for i in unsorted:
        if i not in unique_words:
            unique_words.append(i)
    return unique_words 
print()
print("Unique list:")
finalist = []
finalist = uniqlist(lists_words)
a = len(finalist)-1
for i in range(a):
    print(finalist[i])
    

#print(unique_words.split(), end="\n")


     
