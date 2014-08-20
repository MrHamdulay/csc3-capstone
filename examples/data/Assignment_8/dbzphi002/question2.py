#Thembekile Dubazana
#dbzphi002
#Assignment 8:Q2

"""Number of pairs in a string"""

#The inputs
message=input("Enter a message:\n")
count=0

#The function
def pairs(message):
    global count
    #where will message stop
    if len(message[1:]) ==0:
        return count
    if message[0]==message[1]:
        count+=1
    return pairs(message[2:])#check the rest of the string
    

#Print result
print("Number of pairs:",pairs(message))