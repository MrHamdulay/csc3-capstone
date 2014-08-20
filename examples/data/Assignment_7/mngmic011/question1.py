"""Question 1
Assignment 7
Micaela Menegaldo"""

def strings_list():
    strings={}
    exclusive_strings=[]
    print("Enter strings (end with DONE):")
    word=""
    while word != "DONE":
        word=input("")
        if word not in strings:
            strings[word]=1
            exclusive_strings.append(word)
        else:
            continue
    exclusive_strings=exclusive_strings[:len(exclusive_strings)-1]
    print()
    print("Unique list:")
    for item in exclusive_strings:
        print(item)
    
if __name__=='__main__':
    strings_list()