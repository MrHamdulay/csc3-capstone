"""Raeesa Behardien
BHRRAE003
02 May 2014
Assignment 7
Question 1"""

#create empty list
new_list = []

#ask user for input
string = input("Enter strings (end with DONE):\n")

#keep asking until user enters DONE
while string !="DONE":
   new_list.append (string)
   string = input ("")

#function that removes repeated input
def unique(new_list):
      output = []
      for i in new_list:
         if i not in output:
            output.append(i)
      print("")      
      print("Unique list:")    
      print("\n".join(output))
unique(new_list)