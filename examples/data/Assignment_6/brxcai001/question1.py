#Program where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.
#BRXCAI001
#25 April 2014

#Create an empty list.
strings = []

#Get a list of strings that stops getting strings when DONE is enetered.
string = input("Enter strings (end with DONE):\n")

while string != "DONE":
    strings.append(string)
    string = input("")

#Find the longest string in the list "strings".
maximum = 0
for string in strings:
    if len(string)> maximum:
        maximum = len (string)


#Right justify all the string words with the longest string.
print("\nRight-aligned list:")
for string in strings:
    print(string.rjust(maximum))


   
    

