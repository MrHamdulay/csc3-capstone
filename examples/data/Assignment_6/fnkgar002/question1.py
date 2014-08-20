"""Program to print a list of right-aligned strings
Gary Finkelstein
20 April 2014"""     
     
#creating a blank array to store input values from user    
names = []
#allow user to enter strings while the word "DONE" is not entered
input_name = input("Enter strings (end with DONE): \n")
while input_name != "DONE":
     names.append(input_name)
     input_name = input("")


print("")          
print("Right-aligned list:")    

#creating a string variable to hold the longest word
longest_word = ""
#searching for the longest word in the array and storing that value into the longest word string.
for j in range((len(names))):
     if(len(longest_word) < len(names[j])):
          longest_word = names[j]
#right alining the longest word and the other words by finding the difference in length of the longest word to another word and multiplying a space by this difference in length: 
for i in range (len(names)):
     if(names[i] == longest_word):
          print(longest_word)
          
     else:
          print(" "*(len(longest_word) - len(names[i])) + names[i])
    