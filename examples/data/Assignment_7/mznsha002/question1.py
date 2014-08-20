#28 April 2014
#Shaun Muzenda
#Program where a list of strings is printed out in which duplicates are not printed

string_lst = []      #empty string
inputed_string = input ("Enter strings (end with DONE):\n") 

while inputed_string != "DONE":     #inputing DONE ends the loop
   
   if inputed_string not in string_lst:   #checking whether the inputed word is already in the list or not 
      string_lst.append (inputed_string)     #adding strings to the empty string
   inputed_string = input ("")
 
print() 
   
print("Unique list:")     
for i in string_lst:
      print(i)       #prints the list w/out duplicate words