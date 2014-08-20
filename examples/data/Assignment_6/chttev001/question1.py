#Tevin Chetty
#CHTTEV001
#Question 1

"""22 April 2014
Program to align a list of names"""

list_strings=[] #creates an empty lisy

string=input("Enter strings (end with DONE): \n")
while string!="DONE": #fills list with input
    list_strings.append(string)
    string=input("") #puts all inputs all under each other and stops from appending the same name
    
length=0
for string in list_strings: # To find the maximum length
    current=len(string)
    if current>length:
        length=current
print() #space between input and the aligned list
print("Right-aligned list:")        
for string in list_strings:
    final="{0:>" "{1}}".format(string, length)#when formatting have to use second {} to use variable defined above
    print(final)