#Description: Identifies unique strings from a list of unique strings
#Name: Paul Roux RXXPAU008
#Date: 01 May 2014

def get_entries():
    #Gets strings from the user, ending when the user enters "DONE"
    entry = input("Enter strings (end with DONE):\n")
    while entry != "DONE":
        entries.append(entry)
        entry = input()
    print()

def sort_unique():
    #Identifies the unique strings in the list, storing them in another list
    for i in entries:
        if i not in unique:
            unique.append(i)
        
def print_unique_entries():
    #Prints the list of unique strings
    print("Unique list:")
    for i in unique:
        print(i)
        
if __name__ == "__main__":
    entries = []
    unique = []    
    get_entries()
    sort_unique()
    print_unique_entries()