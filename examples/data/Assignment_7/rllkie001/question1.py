#Kieran Reilly, RLLKIE001
#Delelting the Duplicates
#Assignment 7, Question 1
#01/05/14

tempString = input("Enter strings (end with DONE):\n")
String_list = []
final_list = []

while tempString != "DONE":
    String_list.append(tempString)
    tempString = input("")
    
for i in range(len(String_list)):
    if String_list[i] not in final_list:
        final_list.append(String_list[i])
print("")
print("Unique list:")
for i in range(len(final_list)):
    print(final_list[i])