#glnrus002
#question 1
# 27 April 2014
#Write a Python program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.

def enter_list_of_strings():#get input from user
    user_input=input("Enter strings (end with DONE):\n")
    count=0
    collection_of_input=[]
    collection_of_input.append(user_input)
    while user_input!="DONE":#used to get list from user
        count+=1
        user_input=input("")
        collection_of_input.append(user_input)
    return collection_of_input   
        
def duplicate(collection):#used to creat a duplicate of the input to be used for manipulation
    del collection[len(collection)-1]
    uniques=""
    print("\nUnique list:")
    for i in range(0,len(collection)):        
        if collection[i] not in uniques:
            print(collection[i])
            uniques+=collection[i]
            
if __name__=="__main__":
    collection=enter_list_of_strings()    
    duplicate(collection)