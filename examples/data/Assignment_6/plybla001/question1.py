"""Right alligne a list of words with the longest words
B.Player
20/04/2014"""

#user enters strings into list
words=[]
word=' '
print("Enter strings (end with DONE):")
while word:
   word=input()
   if word!='DONE':
      words.append(word)
   else: break

#find longest word and right alligne
longest_word=0
for word in words:
   if len(word)>longest_word:
      longest_word=len(word)
print("\nRight-aligned list:")

for word in words:
   print("{0:>{1}}".format(word,longest_word))