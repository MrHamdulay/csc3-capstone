"""right align a list of strings
Carla Wilby
19 April 2014"""

#get a list of words
word_list = []
current_string = input("Enter strings (end with DONE):\n")
while current_string != "DONE":
    word_list.append(current_string)
    current_string = input("")

#find longest string
longest_length = 0
for i in word_list:
    if len(i) >= longest_length:        
        longest_length = len(i)

#return right-aligned list
print("\nRight-aligned list:")
for i in word_list:
   print((longest_length-len(i))*" "+i)