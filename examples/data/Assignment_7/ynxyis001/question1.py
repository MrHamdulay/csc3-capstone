#print sentence without duplicates
#Jennifer Yuan (YNXYIS001)
#30 April 2014

sentence = [] #emptty list 
word = input("Enter strings (end with DONE):\n") #asks for input from user
while word != "DONE": #sentinel 
   if word not in sentence: #checks that words are not repeated
      sentence.append(word) #puts words that are not repeated into list
   word = input ("") #gets more input until user types in "DONE" 
   
print("\nUnique list:") #heading

for i in sentence: #prints all words in list with not repeated words
   print(i)