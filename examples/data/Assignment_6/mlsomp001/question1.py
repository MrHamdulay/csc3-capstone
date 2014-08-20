#getting the list aligned to the length of the longest wod
#omphemtse molusi
#MLSOMP001
#25 APRIL 2014




#Get strings
list_names=[]  #name of the list
#entering the strings into the list
lister=input("Enter strings (end with DONE):\n")
while lister!="DONE":
    if lister=="DONE":
        break
    else:
        list_names.append(lister)
        lister=input()

#the length at which the words are gonna be aligned
align_length = 0
for lister in list_names:
    if len(lister) > align_length:
        align_length = len(lister)

#printing out the aligned words
print("\nRight-aligned list:")
for lister in list_names:
    while len(lister) < align_length:
        lister = " " + lister
    print(lister)