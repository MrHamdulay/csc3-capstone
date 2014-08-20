#28 April 2014
#sarayn subroyen
#Program where a list of strings is printed out in which duplicates are not printed

string_list = []                                               #empty string
inputed_string = input ("Enter strings (end with DONE):\n") 

while inputed_string != "DONE":                               #inputing DONE ends the loop
   
   if inputed_string not in string_list:                       #checking for repeats in the list or not 
      string_list.append (inputed_string)                      #adding strings to the empty string without repeats
   inputed_string = input ("")
 
print() 
   
print("Unique list:")     
for i in string_list:
      print(i)                                                #prints the list without repeats