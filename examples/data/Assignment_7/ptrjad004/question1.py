"""Program where a list of strings is printed out in which duplicates are not printed
Jade Petersen
28 April 2014"""

string_list = []   #empty string
inputed_string = input ("Enter strings (end with DONE):\n") 

while inputed_string != "DONE":  #DONE ends the loop
   
   if inputed_string not in string_list:   #identifying whether or not repeats are present 
      string_list.append (inputed_string)  #adding strings to the empty string without repeats
   inputed_string = input ("")
 
print() 
   
print("Unique list:")     
for i in string_list:
      print(i)      #printing the list without repeats