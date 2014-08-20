"""Remove duplicates
B.Player
27/04/2014"""

words = []

#enter words and enter unique into list
word = input("Enter strings (end with DONE):\n")
while word!='DONE':
   if not word in words: words.append(word)
   word = input()
else: print() 
 #Print unique list
 
print("Unique list:")
for word in words:
   print(word)