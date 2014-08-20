""" strings are then printed in the same order but without duplicates.
barak setton
27/04/2014"""

stringlist = []
word = input("Enter strings (end with DONE): \n")

while word != "DONE":
    if word not in stringlist:
        stringlist.append(word)
    word = input()

print()
print("Unique list:")
for i in stringlist:
    print(i)