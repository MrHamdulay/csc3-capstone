# This program asks a user to enter a list of strings with sentinel "DONE"
# The list of strings is then printed out right-aligned with the longest string.

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 22 April 2014

rawlist = [] # strings stored here
listlen = [] # length of the strings stored here
longest = ''

rawinput = input("Enter strings (end with DONE):\n")

# Store strings to the list
while rawinput != "DONE":
    rawlist.append(rawinput)
    rawinput = input()
    
# Store length of strings 
for item in rawlist:
    listlen.append(len(item))
listlen.sort() # sort the lengths in acsending order

if len(listlen) != 0:
    longest = max(listlen) # longest length is now known
else:longest = 0

# print out the list right aligned in a column of width using the longest string
print("\nRight-aligned list:")
for j in rawlist:
    print(" "*(longest-len(j)),j,sep='')


#Sample I/O:

#Enter strings (end with DONE):
#Stuart
#Masixole
#Milan
#Joachim
#Hanan
#Caitlin
#Molefe
#Jason
#Jacob
#Mbongeni
#DONE

#Right-aligned list:
  #Stuart
#Masixole
   #Milan
 #Joachim
   #Hanan
 #Caitlin
  #Molefe
   #Jason
   #Jacob
#Mbongeni