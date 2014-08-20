# Yudhi Moodley
# Assignment 8 - pair letters
# 09/05/2014

store=[]
store1=[]
def pairs(string):
    
    if string == "":
        return 0
    
    else:
        if len(string) > 1:
            if string[0] == string[1]:
                store.append(string[0])
                return pairs (string[2:])
    
            else:
                return pairs (string[1: ])
    
message = input("Enter a message:\n")
pairs(message)
print("Number of pairs:", len(store))