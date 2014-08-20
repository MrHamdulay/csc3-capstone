"""Program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates
Gary Finkelstein
1 May 2014"""

#prompt user to enter words
words = input("Enter strings (end with DONE):\n")

#creat array to store users words
wordsArray=[]
removedDuplicates=[]

count =0
#allow user to enter words into array
while words != "DONE":
    wordsArray.append(words)
    words=input("")

#check to see if the entererd words in the words array exist in the no duplicates array and if not, add them to the no duplicates array
for word in wordsArray:
    if not word in removedDuplicates:
        removedDuplicates.append(word)
        count+=1
       
#print the list without duplicates
print("")
print("Unique list:")
for i in range (count):
    print(removedDuplicates[i])

        
        
