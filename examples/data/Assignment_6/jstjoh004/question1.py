# program to get a list and then print it out right alaigned
# hendrik joosten
# 24/04/2014

# declare empty array to store the strings
words = []

# populate the list
element = input ("Enter strings (end with DONE):\n")
while element != "DONE":
   words.append (element)
   element = input ("")

# declare variable to find the longest string in the array
biggest = 0

#find the longest string
for i in range(len(words)):
   if len(words[i]) > biggest:
      biggest = len(words[i])
      
#print the list, pading with spaces to make everything right alaigned
print("")
print("Right-aligned list:")
for j in range(len(words)):
   print(" "*(biggest - len(words[j])) + words[j])