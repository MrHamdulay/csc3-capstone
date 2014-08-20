#24 April 2014
#Shaun Muzenda
#Program where a list of strings is printed out right aligned to the longest string

string_lst = []      #empty string
inputed_string = input ("Enter strings (end with DONE):\n") 
maximum = 0

while inputed_string != "DONE":     #inputing DONE ends the loop
   
   string_lst.append (inputed_string)     #adding strings to the empty string
   string_length = len(inputed_string)    #finding length of strings
   inputed_string = input ("")
   
   if string_length > maximum:   #finding the longest string in the list
      maximum = string_length
      
print() 

   
print("Right-aligned list:")     
for inputed_string in string_lst:
   print((maximum-(len(inputed_string)))*" "+inputed_string)      #formats the display so the list is roght aligned to the longest string
