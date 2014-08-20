# get a unique list of words
# HLLBRA005
#

words = []
word = input ("Enter strings (end with DONE):\n")
while word != "DONE":
   if word not in words:
      
         words.append (word)
   word = input ("")

# print out the unique list
print("")
print ("Unique list:")
for i in range (len(words)):
   print (words[i])

