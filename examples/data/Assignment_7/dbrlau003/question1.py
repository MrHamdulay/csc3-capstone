#Lauren de Bruyn
#Enter a list of strings and print strings in the same order but without duplicates.
#30 April 2014

#user enter strings which are copied into a list
strings = []
word = input ("Enter strings (end with DONE):\n")
while word != "DONE":
   strings.append (word)
   word = input ("")
   
#create new list without duplicates
newstrings = []
for i in strings:
   if i not in newstrings:
      newstrings.append(i)

#print new list without duplicates
print("\nUnique list:")
for n in newstrings:
   print(n)
      