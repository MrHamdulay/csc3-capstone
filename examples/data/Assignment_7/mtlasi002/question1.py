#Asil Motala
#MTLASI002
#Assignment 7
#Question 1
#27 April 2014

print("Enter strings (end with DONE):\n")             #print instruction for user
list_of_unique_strings=[]                           #initialize list of unique strings
while True:
    string=input("")                                #get user input
    if string=="DONE":                              #create sentinel value
        break                                       #terminate loop with 'DONE'
    else:
        if not string in list_of_unique_strings:    #check for string in list
            list_of_unique_strings.append(string)   #add unique string to list

print("Unique list:")                               #print result for user
for i in list_of_unique_strings:                    #loop through list
    print(i)                                        #print each unique word
    