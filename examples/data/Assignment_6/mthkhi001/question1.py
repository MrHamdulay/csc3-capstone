#MTHKHI001
#Assignment 6
#Question 1

arr = []
user_input = ""
longestword = 0 # counter to find length of longest word, used for allignment
print("Enter strings (end with DONE):")
while user_input != "DONE":
    user_input = input()
    if user_input != "DONE":
        arr.append(user_input)
        if len(user_input)> longestword:
            longestword = len(user_input) # if the length of the new word is greater than that of the previous max, this this becomes the new longestword counter
print()
print("Right-aligned list:")
for i in range (len(arr)):
    count = len(arr[i])
    difference = longestword - count # using difference so that it can be added to the front of the word, to allow for all words to be perfectly right alligned
    print(" "*difference + arr[i])
    
    
    